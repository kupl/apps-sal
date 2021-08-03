class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        ans = 0
        has_ever_flipped = [0] * n
        valid_flip_count_for_current_idx = 0
        for i in range(n):
            if i >= K:
                if has_ever_flipped[i - K] == 1:
                    valid_flip_count_for_current_idx -= 1
            if valid_flip_count_for_current_idx % 2 == A[i]:
                if i + K > n:
                    return -1
                valid_flip_count_for_current_idx += 1
                has_ever_flipped[i] = 1
                ans += 1
        return ans
