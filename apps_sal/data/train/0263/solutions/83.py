from collections import deque


class Solution:

    def knightDialer(self, n: int) -> int:
        neighborMap = {
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: (),
            6: (1, 7, 0),
            7: (2, 6),
            8: (3, 1),
            9: (2, 4),
            0: (4, 6)
        }

        def neighbors(pos):
            return neighborMap[pos]

        def countSeq():
            prevMoves = [1] * 10
            curMoves = [0] * 10
            curN = 1

            while curN < n:
                curMoves = [0] * 10
                curN += 1

                for pos in range(10):
                    for neighbor in neighbors(pos):
                        curMoves[pos] += prevMoves[neighbor]
                prevMoves = curMoves

            curMoves = prevMoves
            # print(curMoves)
            return sum(curMoves)

        # totalSeq = 0
        # for curPos in range(10):
        #     totalSeq += countSeq(curPos)

        return countSeq() % (10**9 + 7)


# Prev implementation
#     def knightDialer(self, n: int) -> int:
#         def inPad(row, col):
#             if row >= 0 and row < 3 and col >= 0 and col < 3 or (row == 3 and col == 1):
#                 return True
#             return False

#         dRows = [1,-1,1,-1,2,-2,2,-2]
#         dCols = [2,2,-2,-2,1,-1,-1,1]

#         q = deque()
#         q.append((3,1,n-1))

#         for i in range(3):
#             for j in range(3):
#                 q.append((i,j, n-1))

#         distinctNums = 0
#         while q:
#             cur = q.popleft()

#             if cur[2] == 0:
#                 distinctNums += 1
#                 continue

#             for dRow, dCol in zip(dRows, dCols):
#                 newRow, newCol = cur[0] + dRow, cur[1] + dCol

#                 if inPad(newRow, newCol):
#                     q.append((newRow, newCol, cur[2] - 1))

#         return distinctNums % (10**9 + 7)
