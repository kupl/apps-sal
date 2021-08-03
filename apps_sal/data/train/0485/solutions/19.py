class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        count = 0
        flippings = [False for _ in A]
        flipped = False
        for i in range(len(A)):
            if flippings[i]:
                flipped = not flipped
            if (not flipped and A[i] == 0) or (flipped and A[i] == 1):
                count += 1
                flipped = not flipped
                if i + K > len(A):
                    return -1
                if i + K < len(flippings):
                    flippings[i + K] = True

        return count
