class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        total_flips = 0
        current_effective_flips = 0
        flip_indices = []

        for current_index, elem in enumerate(A):
            if (flip_indices and current_index == flip_indices[0] + K):
                flip_indices.pop(0)
                current_effective_flips -= 1

            if self.needs_flip(elem, current_effective_flips):
                if current_index + K > len(A):
                    return -1
                flip_indices.append(current_index)
                current_effective_flips += 1
                total_flips += 1
        return total_flips

    def needs_flip(self, elem, current_effective_flips):
        return ((elem == 0 and current_effective_flips % 2 == 0) or
                (elem == 1 and current_effective_flips % 2 != 0))
