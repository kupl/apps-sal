class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        '''
        102

        A -- not -> B

        B <= 0.5A + 7
        B > A
        ~ B > 100 & A < 100

        split to > 100, < 100 groups


        right to left, > 100 region

        '''

        count = [0] * 121
        for age in ages:
            count[age] += 1

        res = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):

                if (ageA * 0.5 + 7 >= ageB):
                    continue
                if (ageA < ageB):
                    continue
                if (ageA < 100 and ageB > 100):
                    continue

                res += countA * countB
                if ageA == ageB:
                    res -= countA
        return res
