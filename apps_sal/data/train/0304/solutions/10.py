class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_cnt = [0] * 121
        for age in ages:
            age_cnt[age] += 1

        res = 0
        for ageA, cntA in enumerate(age_cnt):
            for ageB, cntB in enumerate(age_cnt):
                if ageB <= (0.5 * ageA + 7) or ageB > ageA or (ageB > 100 and ageA < 100):
                    continue
                res += (cntA * cntB)
                if ageA == ageB:
                    res -= cntA
        return res
