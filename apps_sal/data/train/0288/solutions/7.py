class Solution(object):

    def flipLights(self, lightNum, performTime):
        if lightNum == 0:
            return 0
        if performTime == 0:
            return 1
        if lightNum == 1:
            return 2
        statuNumToStatu = dict()
        statuNumToStatu[0] = (False,) * lightNum
        statuNumToStatu[1] = (True,) * lightNum
        statuNumToStatu[2] = tuple((True if i % 2 == 0 else False for i in range(1, lightNum + 1)))
        statuNumToStatu[3] = tuple((True if i % 2 == 1 else False for i in range(1, lightNum + 1)))
        statuNumToStatu[4] = tuple((True if i % 3 == 1 else False for i in range(1, lightNum + 1)))
        statuNumToStatu[4] = tuple((True if i % 3 == 1 else False for i in range(1, lightNum + 1)))
        statuNumToStatu[1, 4] = tuple((True if i % 3 != 1 else False for i in range(1, lightNum + 1)))
        statuNumToStatu[2, 4] = tuple((True if (i % 2 == 0) ^ (i % 3 == 1) else False for i in range(1, lightNum + 1)))
        statuNumToStatu[3, 4] = tuple((True if (i % 2 == 1) ^ (i % 3 == 1) else False for i in range(1, lightNum + 1)))
        statuNumToNextStatuNums = {0: [1, 2, 3, 4], 1: [0, 2, 3, (1, 4)], 2: [0, 1, 3, (2, 4)], 3: [0, 1, 2, (3, 4)], 4: [0, (1, 4), (2, 4), (3, 4)], (1, 4): [1, 4, (2, 4), (3, 4)], (2, 4): [2, 4, (1, 4), (3, 4)], (3, 4): [3, 4, (1, 4), (2, 4)]}
        prevStatuNums = {0}
        for eachTime in range(performTime):
            nextStatuNums = set()
            for eachStatuNum in prevStatuNums:
                for eachNextStatu in statuNumToNextStatuNums[eachStatuNum]:
                    nextStatuNums.add(eachNextStatu)
            prevStatuNums = nextStatuNums
        allStatus = set()
        for eachStatuNum in prevStatuNums:
            allStatus.add(statuNumToStatu[eachStatuNum])
        return len(allStatus)
