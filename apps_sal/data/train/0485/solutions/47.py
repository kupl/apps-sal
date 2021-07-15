class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flips = collections.deque()

        result = 0
        for i, num in enumerate(A):
            if A[i] == (len(flips) & 1):
                result += 1
                flips.append(i + K - 1)
            while flips and flips[0] <= i:
                flips.popleft()

        return result if len(flips) == 0 else -1

