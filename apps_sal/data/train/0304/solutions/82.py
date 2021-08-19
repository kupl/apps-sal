class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        agesCount = [0] * 121
        for age in ages:
            agesCount[age] += 1

        res = 0
        for i in range(1, 121):
            for j in range(1, 121):
                if agesCount[i] == 0 or agesCount[j] == 0 or j > i or (j > 100 and i < 100) or (j <= i / 2 + 7):
                    continue

                res += agesCount[i] * agesCount[j]
                if i == j:
                    res -= agesCount[i]  # because I can't send request to myself

        return res
