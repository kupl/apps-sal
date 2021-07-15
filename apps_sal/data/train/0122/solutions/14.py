class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = [0], [0]
        for i in range(k):
            left.append(left[-1]+ cardPoints[i])
            right.append(right[-1] + cardPoints[len(cardPoints) -1 - i])
        
        res  = 0 
        for i in range(k+1):
            
            x = left[i] + right[k-i]
            res = max(res,x)
            
        return res
            

#         front_sum=back_sum=[0]
#                 print 'cardPoints:', cardPoints
#         print 'k:', k
#         frontSum, backSum = [0], [0]
#         for n in cardPoints:
#             frontSum.append(frontSum[-1]+n)
#             print 'frontSum:', frontSum
#         for n in cardPoints[::-1]:
#             backSum.append(backSum[-1]+n)
#             print 'backSum:', backSum
#         allCombinations = [frontSum[i]+backSum[k-i] for i in range(k+1)]
#         print 'allCombinations:', allCombinations
#         return max(allCombinations)

