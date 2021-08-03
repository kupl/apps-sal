class Solution:
    def minKBitFlips(self, A: List[int], k: int) -> int:
        k_bit_flip_end_indices = deque()
        switch = 0
        flips = 0
        for i, bit in enumerate(A):
            if (len(k_bit_flip_end_indices) & 1) ^ bit == 0:
                flips += 1
                k_bit_flip_end_indices.append(i + k - 1)
            if k_bit_flip_end_indices and i == k_bit_flip_end_indices[0]:
                k_bit_flip_end_indices.popleft()
        return flips if not k_bit_flip_end_indices else -1
