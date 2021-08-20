class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1
        res = 0
        for (ageA, countA) in enumerate(count):
            for (ageB, countB) in enumerate(count):
                if ageB <= ageA * 0.5 + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue
                res += countA * countB
                if ageA == ageB:
                    res -= countA
        return res
