class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1
        res = 0 
        for age_a, count_a in enumerate(count):
            for age_b, count_b in enumerate(count):
                if age_b <= 0.5 * age_a + 7:
                    continue 
                if age_b > age_a:
                    continue 
                if age_b > 100 and age_a < 100:
                    continue 
                res += count_a * count_b
                if age_a == age_b:
                    res -= count_a
        return res
