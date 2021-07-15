class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        cur, res = 0, 0
        
        for i in range(len(A)):
            # to check if A[i-K] has been flipped
            if i >= K and A[i-K] > 1:
            # since i-K is out of the sliding window, need to substract the total flip number by 1
                cur -= 1
                
            if (cur%2)^A[i] == 0:
                if i + K > len(A):
                    return -1
                
                A[i] += 2
                cur += 1
                res += 1
                
        return res

