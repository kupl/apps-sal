class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        memo = {}

        def helper(a, b):
            if a == b:
                return 0
            if (a, b) in memo:
                return memo[a, b]
            res = float('inf')
            if a[-1] == b[-1]:
                res = min(res, helper(a[:-1], b[:-1]))
            else:
                for i in range(len(a) - 1):
                    if a[i] == b[-1] and a[i] != b[i]:
                        a_new = a[:i] + a[-1] + a[i + 1:-1]
                        res = min(res, 1 + helper(a_new, b[:-1]))
            memo[a, b] = res
            return res
        return helper(A, B)
        '\n        # 这道题虽然是hard但是通过你理解题意，很容易找到潜在的解答方法。\n        # 第一重思路就是看到最小。那么只要比最小的大都OK，那么很容易想到用二分法去猜测答案。但是如何check存疑\n        # 第二重思路就是看到两个node。第一个node通过交换变成第二个。交换的可能性很多。因此可以看乘bfs\n        # BFS就是给你一个起点一个终点，问你最近的距离，最少的方式等等是多少！\n        # by build directed edges bfs to find k\n        def neighbor(x):\n            i = 0\n            while x[i] == B[i]:  # 更换的种类很多种，但是仍然需要剪枝无效的。因此相同部分就不改变了。\n                i += 1\n            for j in range(i + 1, len(x)): # 找到第一个不同的地方，然后去找可以过来填坑的letter\n                if x[j] == B[i]:\n                    yield x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]\n        q, seen = [(A, 0)], {A}\n        for x, d in q:\n            if x == B:\n                return d\n            for y in neighbor(x):\n                if y not in seen:\n                    seen.add(y)\n                    q.append((y, d + 1))\n        '
