class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        buckets = [0] * 121
        for age in ages:
            buckets[age] += 1

        ans = 0
        for i in range(1, 121):
            if buckets[i] <= 0:
                continue
            for j in range(1, 121):
                if buckets[j] <= 0:
                    continue

                if j <= 0.5 * i + 7 or j > i or (j > 100 and i < 100):
                    continue

                ans += buckets[i] * buckets[j]
                if i == j:
                    ans -= buckets[i]

        return ans
