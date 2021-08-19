class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        age_range = [0] * 121

        ages = sorted(ages)

        ans = 0

        for age in ages:

            for i in range(age - 1, -1, -1):

                if i <= 0.5 * age + 7:
                    break

                ans += age_range[i]

#             it is tricky here, becareful
            if age > 0.5 * age + 7:
                ans += age_range[age] * 2

            age_range[age] += 1

        return ans
