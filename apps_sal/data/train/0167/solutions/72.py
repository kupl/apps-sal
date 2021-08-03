class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        num_moves = [n for n in range(N + 1)]

        for k in range(2, K + 1):
            next_num_moves = [0 for _ in range(N + 1)]
            floor = 1
            for n in range(1, N + 1):
                safe_moves = next_num_moves[n - floor]
                unsafe_moves = num_moves[floor - 1]
                nk_moves = 1 + max(safe_moves, unsafe_moves)
                while floor < N:
                    next_floor = floor + 1
                    next_safe_moves = next_num_moves[n - next_floor]
                    next_unsafe_moves = num_moves[next_floor - 1]
                    next_nk_moves = 1 + max(next_safe_moves, next_unsafe_moves)
                    if next_nk_moves < nk_moves:
                        floor = next_floor
                        nk_moves = next_nk_moves
                    else:
                        break
                next_num_moves[n] = nk_moves
            num_moves = next_num_moves
        return num_moves[N]
