class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        flip_pos = 0
        flip_inds = []
        for i in range(len(A)):
            while flip_pos < len(flip_inds) and i - K + 1 > flip_inds[flip_pos]:
                flip_pos += 1
            is_flipped = False
            if (len(flip_inds) - flip_pos) % 2 != 0:
                is_flipped = True
            cur_bit = A[i]
            if is_flipped:
                cur_bit = not cur_bit
            if i > len(A) - K:
                if cur_bit == 0:
                    return -1
            elif not cur_bit:
                flip_inds.append(i)
        return len(flip_inds)
