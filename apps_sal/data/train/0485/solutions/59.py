class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flips = collections.deque()
        res = 0
        for i, a in enumerate(A):
            if (A[i] != 0 and len(flips) & 1) or (not len(flips) & 1 and A[i] != 1):
                res += 1
                flips.append(i + K - 1)
            while flips and flips[0] <= i:
                flips.popleft()
        return res if not flips else -1
