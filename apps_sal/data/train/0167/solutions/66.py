class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}

        def num_moves(n, k):
            if (n, k) not in dp:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    left = 1
                    right = n + 1
                    while left < right:
                        floor = (left + right) // 2
                        safe_moves = num_moves(n - floor, k)
                        unsafe_moves = num_moves(floor - 1, k - 1)
                        if safe_moves > unsafe_moves:
                            left = floor + 1
                        else:
                            right = floor

                    floor = left
                    safe_moves = num_moves(n - floor, k)
                    unsafe_moves = num_moves(floor - 1, k - 1)
                    nk_moves = max(safe_moves, unsafe_moves) + 1

                    if floor > 1:
                        prev_floor = left - 1
                        prev_safe_moves = num_moves(n - prev_floor, k)
                        prev_unsafe_moves = num_moves(prev_floor - 1, k - 1)
                        prev_nk_moves = max(prev_safe_moves, prev_unsafe_moves) + 1
                        nk_moves = min(nk_moves, prev_nk_moves)
                    ans = nk_moves
                dp[(n, k)] = ans
            return dp[(n, k)]
        return num_moves(N, K)
