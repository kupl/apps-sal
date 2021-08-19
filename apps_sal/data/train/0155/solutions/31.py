class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        jumps = defaultdict(list)

        def check(it):
            stack = []
            for i in it:
                while stack and arr[stack[-1]] < arr[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        jumps[j].append(i)
                stack.append(i)
        N = len(arr)
        check(range(N))
        check(reversed(range(N)))

        @lru_cache(None)
        def dfs(i):
            return 1 + max((dfs(j) for j in jumps[i]), default=0)
        return max((dfs(i) for i in range(N)))
