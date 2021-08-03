class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        sorted_indexes = sorted(range(len(arr)), key=lambda i: arr[i])
        n = len(arr)
        dp = [1] * n

        def get_neighs(cur):
            neighs = []
            directions = [1, -1]
            for dire in directions:
                for i in range(cur + dire, cur + (d + 1) * dire, dire):
                    if i < 0 or i >= n:
                        break
                    if arr[i] >= arr[cur]:
                        break
                    neighs.append(i)
            return neighs

        for cur in sorted_indexes:
            for neigh in get_neighs(cur):
                dp[cur] = max(dp[cur], dp[neigh] + 1)
        return max(dp)
