class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        odd_jumps = {}
        stack = []
        for num, i in sorted([[num, i] for i, num in enumerate(A)], reverse=True):
            while stack and stack[-1][1] < i:
                stack.pop()
            if not stack:
                odd_jumps[i] = None
            else:
                odd_jumps[i] = stack[-1][1]
            stack.append([num, i])

        even_jumps = {}
        stack = []
        for num, i in sorted([[num, -i] for i, num in enumerate(A)]):
            i = -i
            while stack and stack[-1][1] < i:
                stack.pop()
            if not stack:
                even_jumps[i] = None
            else:
                even_jumps[i] = stack[-1][1]
            stack.append([num, i])

        n = len(A)

        @lru_cache(None)
        def dfs(i, is_odd):
            if i == n - 1:
                return True
            if is_odd and odd_jumps[i]:
                return dfs(odd_jumps[i], False)
            elif not is_odd and even_jumps[i]:
                return dfs(even_jumps[i], True)
            else:
                return False

        res = 0
        for i in range(n):
            res += 1 if dfs(i, True) else 0
        return res
