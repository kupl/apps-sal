class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        valid_ages = [0] * 121
        for age in ages:
            valid_ages[age] += 1

        count = 0
        for i in range(1, 121):
            ageA = valid_ages[i]
            for j in range(1, 121):
                ageB = valid_ages[j]
                if j <= 0.5 * i + 7 or j > i:
                    continue
                if j > 100 and i < 100:
                    continue
                count += ageA * ageB
                if i == j:
                    count -= ageA
        return count
