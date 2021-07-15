class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        requests = 0
        ageCount = [0] * 121
        for age in ages:
            ageCount[age] += 1

        for A in range(120, 14, -1):
            if not ageCount[A]:
                continue
            requests += (ageCount[A] * (ageCount[A] - 1))
            for B in range(A-1, int(0.5*A + 7), -1):
                requests += (ageCount[A] * ageCount[B])
        return requests
