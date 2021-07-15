class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flip_ends = deque()
        count = 0
        for (idx, bit) in enumerate(A):
            if len(flip_ends) > 0 and idx >= flip_ends[0]:
                flip_ends.popleft()
            val = (bit + len(flip_ends)) % 2
            if val == 1:
                continue

            if idx + K > len(A):
                return -1

            count += 1
            flip_ends.append(idx + K)

        return count

