class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # dp = {prev_val, next_val: len}
        dp = {}
        dp[(A[1], A[0] + A[1])] = 2
        for i in range(2, len(A)):
            for j in range(i):
                if (A[j], A[i]) not in dp:
                    dp[(A[i], A[j] + A[i])] = 2
                else:
                    dp[(A[i], A[j] + A[i])] = dp[(A[j], A[i])] + 1
                    del dp[(A[j], A[i])]
                #print(A[i], A[j], dp)
        longest = max(dp.values())
        
        return longest if longest > 2 else 0
        
        

