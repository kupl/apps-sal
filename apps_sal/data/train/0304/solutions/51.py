class Solution:
    def numFriendRequests(self, ages) -> int:
        ages = Counter(ages)
        ans = 0
        for age_a, count_a in ages.items():
            for age_b, count_b in ages.items():
                if age_a * 0.5 + 7 >= age_b:
                    continue
                if age_a < age_b:
                    continue
                if age_a < 100 and age_b > 100:
                    continue
                ans += count_a * count_b
                if age_a == age_b:
                    ans -= count_a
        return ans
