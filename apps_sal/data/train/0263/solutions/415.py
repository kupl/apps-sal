class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        move = [1]*10
        for i in range(n-1):
            new_move = [1]*10
            new_move[0], new_move[1] = (move[4]+move[6])%(10**9 + 7), (move[8]+move[6])%(10**9 + 7)
            new_move[2], new_move[3] = (move[7]+move[9])%(10**9 + 7), (move[8]+move[4])%(10**9 + 7)
            new_move[4], new_move[5] = (move[0]+move[3]+move[9])%(10**9 + 7), 0
            new_move[6], new_move[7] = (move[0]+move[1]+move[7])%(10**9 + 7), (move[2]+move[6])%(10**9 + 7)
            new_move[8], new_move[9] = (move[1]+move[3])%(10**9 + 7), (move[2]+move[4])%(10**9 + 7)
            move = new_move
        return sum(move) % (10**9 + 7)

