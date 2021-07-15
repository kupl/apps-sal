class Solution:
    def minKBitFlips(self, A, K):
        cur, res, n = 0, 0, len(A)    # cur is number of flip since start of current window
        for i in range(len(A)):
            if i >= K and A[i - K] > 1:
                A[i - K] -= 2
                cur -= 1
            if cur & 1 ^ A[i] == 0: # first module 2, even flip is no flip, odd flip is one flip
                if i + K > len(A):
                    return -1
                A[i] += 2
                cur += 1
                res += 1
        return res
    
    def minKBitFlips(self, A, K):
        # cur is number of flip since start of current window
        cur = res = 0
        for i in range(len(A)):
            if i >= K and A[i - K] == 2:  # if we flippped at k, that mean from now on, the flip impact is gone. 
                cur -= 1
             # first module 2, even flip is no flip, odd flip is one flip
            if (cur % 2) == A[i]:
                if i + K > len(A):
                    return -1
                A[i] = 2 # mark flipped at i
                cur, res = cur + 1, res + 1
        return res
