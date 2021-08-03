class Solution:
    def maxLength(self, arr: List[str]) -> int:

        dp = defaultdict(lambda: set())

        def dfs(index, cur):

            if index == len(arr) or cur in dp[index]:
                return len(cur)
            dp[index].add(cur)

            best = len(cur)

            for x in range(index, len(arr)):
                count = Counter(cur)
                xCount = Counter(arr[x])
                canTake = True
                for k, v in xCount.items():
                    if k in count or v > 1:
                        canTake = False
                if canTake:
                    best = max(best, dfs(x + 1, cur + arr[x]))
                best = max(best, dfs(x + 1, cur))

            return best

        return dfs(0, '')
