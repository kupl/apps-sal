from collections import Counter


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        dic = Counter(ages)
        res = 0
        for ageA, cntA in list(dic.items()):
            for ageB, cntB in list(dic.items()):
                if (ageB <= 0.5 * ageA + 7) or (ageB > ageA) or (ageB > 100 and ageA < 100):
                    continue

                res += cntA * cntB

                if ageA == ageB:
                    res -= cntA

        return res
