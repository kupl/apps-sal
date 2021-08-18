class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = [0] * 121
        for age in ages:
            age_count[age] += 1

        res = 0
        print(len(age_count))
        for i in range(121):
            for j in range(121):
                if age_count[i] > 0 and age_count[j] > 0:
                    if j <= 0.5 * i + 7 or j > i:
                        continue
                    res += age_count[i] * age_count[j]
                    if i == j:
                        res -= age_count[i]

        return res
