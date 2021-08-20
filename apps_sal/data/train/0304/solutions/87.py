class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        agesToCount = [0] * 121
        for age in ages:
            agesToCount[age] += 1
        result = 0
        for ageA in range(1, 121):
            for ageB in range(1, 121):
                if ageB <= ageA and ageB > 0.5 * ageA + 7:
                    if ageA == ageB:
                        result += agesToCount[ageA] * (agesToCount[ageA] - 1)
                    else:
                        result += agesToCount[ageA] * agesToCount[ageB]
        return result
