class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flips = collections.deque()
        cnt = 0
        for i in range(len(A)):
            while flips and flips[0] <= i - K:
                flips.popleft()
            curtStatus = A[i] + len(flips)

            if curtStatus % 2 == 0:
                if i > len(A) - K:
                    return -1
                else:
                    flips.append(i)
                    cnt += 1
        return cnt
