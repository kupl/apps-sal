class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        def find(node):
            if parent[node] < 0:
                return node
            else:
                return find(parent[node])

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            p1_size = abs(parent[p1])
            p2_size = abs(parent[p2])
            if p1_size == m or p2_size == m:
                ans = count
            if p1_size < p2_size:
                tmp = parent[p1]
                parent[p1] = p2
                parent[p2] += tmp
            else:
                tmp = parent[p2]
                parent[p2] = p1
                parent[p1] += tmp

        n = len(arr)
        ans = -1

        parent = [-1] * (n + 1)
        bitvalue = [0] * (n + 1)
        for count, i in enumerate(arr, 1):
            if i + 1 <= n and bitvalue[i + 1] == 1 and i - 1 > 0 and bitvalue[i - 1] == 1:
                if abs(parent[find(i + 1)]) == m or abs(parent[find(i - 1)]) == m:
                    ans = count - 1
                union(i, i + 1)
                union(i, i - 1)
            elif i + 1 <= n and bitvalue[i + 1] == 1:
                if abs(parent[find(i + 1)]) == m:
                    ans = count - 1
                union(i, i + 1)
            elif i - 1 > 0 and bitvalue[i - 1] == 1:
                if abs(parent[find(i - 1)]) == m:
                    ans = count - 1
                union(i, i - 1)
            bitvalue[i] = 1
            if abs(parent[find(i)]) == m:
                ans = count
        return ans
