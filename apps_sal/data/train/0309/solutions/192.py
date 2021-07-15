class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ##pretty sure this soln works, it just takes too long.
#         def searchList(num: int, lst: List[int]) -> bool:
#             for curr in lst:
#                 if curr == num:
#                     return True
#             return False
        
#         longest = 2 #shorest array we're given is 2        
#         info = []
#         subseq = {
#             'diff': A[1] - A[0],
#             'seq': A[0:2]
#         }
#         info.append(subseq)
        
        
#         for i in range(2, len(A)):
#             seen = []
#             curr = A[i]
#             prev = A[i - 1]
#             for sub in info:
#                 if curr - sub['seq'][-1] == sub['diff']:
#                     sub['seq'].append(curr)
#                     seen.append(sub['seq'][-1])
#                     if len(sub['seq']) > longest:
#                         longest = len(sub['seq'])            
#             for num in A[0:i]:
#                 #if an element hasn't been seen, append another info subseq dict
#                 #with the current element and the unseen one
#                 if not searchList(num, seen):
#                     diff = curr - num
#                     #if curr + diff < 0, then we know that the subseq will not continue, so don't
#                     #bother keeping it
#                     if curr + diff >= 0:
#                         info.append({
#                             'diff': curr - num,
#                             'seq': [num, curr]
#                         })
#         return longest

        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())
