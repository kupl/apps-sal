class Solution:
    from collections import defaultdict

    def knightDialer(self, N: int) -> int:
        pos_mapping = [[4, 6], [6, 8], [9, 7], [4, 8], [9, 3, 0], [], [7, 1, 0], [6, 2], [1, 3], [4, 2]]

        total_count = 0
        for i in range(10):
            prev_arr = [0] * 10
            prev_arr[i] = 1
            for _ in range(N - 1):
                new_arr = [0] * 10
                for idx in range(10):
                    if prev_arr[idx] == 0:
                        continue
                    for next_pos in pos_mapping[idx]:
                        new_arr[next_pos] += prev_arr[idx]
                prev_arr = new_arr
            total_count += sum(prev_arr)
        MOD = 10**9 + 7
        return total_count % MOD
