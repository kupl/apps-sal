class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:

        flips = collections.deque()

        res = 0
        for i in range(len(A)):
            if A[i] == (len(flips) % 2):
                res += 1
                flips.append(i + K - 1)

            if flips and flips[0] <= i:
                flips.popleft()
        return res if not flips else -1
