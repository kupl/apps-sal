class Solution:
 

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for i in range(n)]
        result = 2
        
        for i in range(1, n):
            for j in range(i):
                delta = A[i] - A[j]
                
                # If we've seen this delta with dp[j], then increase the length of the subseq by 1.
                # This is equivalent of dp[i] 'adding on' to the subsequence.
                if delta in dp[j]:
                    currentLength = dp[j].get(delta)
                    dp[i][delta] = currentLength + 1
                
                else:
                    dp[i][delta] = 2
                
                result = max(result, dp[i][delta])        
        return result
    
    def longestArithSeqLength2(self, A: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        cnt
        arith = [Counter() for i in range(len(A))]
        longest = 0
        for i in range(len(A)-2, -1,-1):
            for j in range(i+1, len(A)):
                diff = A[j]-A[i]
                arith[i][diff] = max(1 + arith[j][diff], arith[i][diff])
                longest = max(longest, arith[i][diff])
        #print(arith)
        
        #         for i in range(len(A)):
        #             #print(arith[i])
        #             most_common = arith[i].most_common()

        #             longest = max(most_common[0][1] if most_common else 0, longest)
        return longest + 1
        # for i in range(len(A)):
        #     for j in range(i+1, len(A)):
        #         cnt[A[j]-A[i]] += 1
        #     print(A[i], cnt)
        # print(cnt)
        # val = cnt.most_common()[0][1]
        # return val + 1 
            
        
        #         self.arith = [dict() for i in range(len(A))]

        #         def helper(i, diff):
        #             if diff in self.arith[i]:
        #                 return self.arith[i][diff]

        #             val = 0
        #             for j in range(i+1, len(A)):
        #                 if A[j] - A[i] == diff:
        #                     val = 1 + helper(j, diff)
        #                     break
        #             self.arith[i][diff] = val        
        #             return self.arith[i][diff]
        

