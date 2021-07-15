class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        i = 0
        ans = 0
        flips = 0
        dq = collections.deque()
        while i < len(A):
            while dq and i >= dq[0]:
                dq.popleft()
                flips -= 1
            if (A[i] + flips) %2 == 1:
                i += 1
            else:
                if i + K > len(A):
                    return -1
                dq.append(i+K)
                flips += 1
                i += 1
                ans += 1
        return ans
                

