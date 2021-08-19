class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        ALen = len(A)
        moves = [[None, None] for i in range(ALen)]  # [odd move, even move]
        sortedNum = [[A[-1], ALen - 1]]

        def insertAt(x):
            l = 0
            r = len(sortedNum) - 1
            if x < sortedNum[l][0]:
                return 0
            if x > sortedNum[r][0]:
                return r + 1
            while r > l:
                m = (r + l) // 2
                if x > sortedNum[m][0]:
                    l = m + 1
                elif x < sortedNum[m][0]:
                    r = m
                else:
                    return m
            return l

        for i in range(ALen - 2, -1, -1):
            i1 = insertAt(A[i])
            if i1 < len(sortedNum) and sortedNum[i1][0] == A[i]:
                moves[i] = [sortedNum[i1][1], sortedNum[i1][1]]
                sortedNum[i1][1] = i
            else:
                if i1 == 0:
                    moves[i][0] = sortedNum[0][1]
                    moves[i][1] = None
                elif i1 == len(sortedNum):
                    moves[i][0] = None
                    moves[i][1] = sortedNum[-1][1]
                else:
                    moves[i] = [sortedNum[i1][1], sortedNum[i1 - 1][1]]
                sortedNum.insert(i1, [A[i], i])
        # print(sortedNum)
        # print(moves)
        goodMoveList = [[False, False] for i in range(ALen)]  # [odd move, even move]
        goodMoveList[-1] = [True, True]
        ans = 1
        for i in range(ALen - 2, -1, -1):
            if moves[i][0] != None and goodMoveList[moves[i][0]][1]:
                goodMoveList[i][0] = True
                ans += 1
            if moves[i][1] != None and goodMoveList[moves[i][1]][0]:
                goodMoveList[i][1] = True
        # print(goodMoveList)
        return ans
