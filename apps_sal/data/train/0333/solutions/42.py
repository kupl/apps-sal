class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if not arr or len(arr) == 1:
            return 0
        dp = [float('inf')] * len(arr)
        dp[0] = 0
        position = collections.defaultdict(set)
        visited = {}
        for (i, e) in enumerate(arr):
            position[e].add(i)
            visited[i] = False
        visited[0] = True
        start = {0}
        step = 0
        while start:
            nextstart = set()
            for i in start:
                if i == len(arr) - 1:
                    return step
                if i - 1 >= 0 and (not visited[i - 1]):
                    dp[i - 1] = min(dp[i - 1], dp[i] + 1)
                    nextstart.add(i - 1)
                    visited[i - 1] = True
                if i + 1 < len(arr) and (not visited[i + 1]):
                    dp[i + 1] = min(dp[i + 1], dp[i] + 1)
                    nextstart.add(i + 1)
                    visited[i + 1] = True
                for p in position[arr[i]]:
                    if p != i and (not visited[p]):
                        dp[p] = min(dp[p], dp[i] + 1)
                        nextstart.add(p)
                        visited[p] = True
                position[arr[i]] = set()
            start = nextstart
            step += 1
