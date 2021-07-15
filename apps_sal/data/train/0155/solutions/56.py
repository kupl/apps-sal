class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        sorted_indexes = sorted(range(len(arr)), key = lambda i:arr[i])
        # print(sorted_indexes)
        n = len(arr)
        dp = [1] * n
        
        def get_neighs(cur):
            neighs = []
            for i in range(cur + 1, min(cur + d + 1, n)):
                if arr[i] < arr[cur]:
                    neighs.append(i)
                else:
                    break
            for i in range(cur - 1, max(cur - d - 1, -1), -1):
                if arr[i] < arr[cur]:
                    neighs.append(i)
                else:
                    break
            return neighs
        
        for cur in sorted_indexes:
            neighs = get_neighs(cur)
            for neigh in neighs:
                dp[cur] = max(dp[cur], dp[neigh] + 1)
        return max(dp)
