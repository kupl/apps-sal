class Solution:
    def numFriendRequests(self, ages) -> int:
        ages = collections.Counter(ages)
        ans = 0
        for ageA, countA in list(ages.items()):
            for ageB, countB in list(ages.items()):
                if ageA * 0.5 + 7 >= ageB:
                    continue
                if ageA < ageB:
                    continue
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA
        return ans
