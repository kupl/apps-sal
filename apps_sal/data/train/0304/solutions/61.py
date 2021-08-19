class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        age_counts = [0] * 121
        for age in ages:
            age_counts[age] += 1
        request_count = 0
        for (ageA, age_countA) in enumerate(age_counts):
            for (ageB, age_countB) in enumerate(age_counts):
                if ageB <= 0.5 * ageA + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageA < 100 < ageB:
                    continue
                request_count += age_countA * age_countB
                if ageA == ageB:
                    request_count -= age_countA
        return request_count
