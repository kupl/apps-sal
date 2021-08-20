class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        max_less_than = []

        def jump(iter):
            res = [None for i in range(len(arr))]
            stack = deque([])
            for i in iter:
                while stack and abs(i - stack[0]) > d:
                    stack.popleft()
                while stack and arr[i] > arr[stack[-1]]:
                    latest_poped = stack.pop()
                    res[latest_poped] = i
                stack.append(i)
            return res
        max_less_than.append(jump(range(len(arr))))
        max_less_than.append(jump(reversed(range(len(arr)))))

        @lru_cache(None)
        def dp(i):
            if i is None:
                return 0
            return max(map(dp, [max_less_than[0][i], max_less_than[1][i]]), default=0) + 1
        return max(map(dp, range(len(arr))))
