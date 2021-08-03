class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for i, x in enumerate(A)}
        longest = 0

        board = []
        for i in range(len(A)):
            row = []
            row = [2] * len(A)
            board.append(row)

        for j in range(len(A)):
            for k in range(j + 1, len(A)):
                a = A[k] - A[j]
                if a < A[j]:
                    i = index.get(a, None)
                    if i != None:
                        board[j][k] = board[i][j] + 1
                        longest = max(longest, board[j][k])

        return longest
