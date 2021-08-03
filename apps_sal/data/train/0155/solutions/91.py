class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        jumps = [1] * n

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

        @lru_cache(None)
        def dp(cur):
            for neigh in get_neighs(cur):
                jumps[cur] = max(jumps[cur], dp(neigh) + 1)
            return jumps[cur]

        for i in range(len(arr)):
            dp(i)
        return max(jumps)
