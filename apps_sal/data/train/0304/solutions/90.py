class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages)
        ans = 0
        for i in count:
            for j in count:
                if not (j <= i * 0.5 + 7 or j > i):
                    ans += count[i] * count[j]
                    if j == i:
                        ans -= count[i]
        return ans
