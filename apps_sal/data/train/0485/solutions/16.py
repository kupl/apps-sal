class Solution:

    def minKBitFlips(self, A: List[int], k: int) -> int:
        flipped = collections.deque()
        flips = 0
        for i in range(len(A)):
            if flipped and flipped[0] < i:
                flipped.popleft()
            if not (len(flipped) & 1) - A[i]:
                if i <= len(A) - k:
                    flips += 1
                    flipped.append(i + k - 1)
                else:
                    return -1
        return flips
