class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        min_len = len(cardPoints) - k
        curr_sum = 0
        min_val = 0
        for start in range(len(cardPoints) - min_len + 1):
            if start == 0:
                curr_sum = sum(cardPoints[start:start+min_len])
                min_val = curr_sum
            else:
                curr_sum = curr_sum - cardPoints[start - 1] + cardPoints[start+min_len-1] 
                if min_val > curr_sum:
                    min_val = curr_sum
        
        return sum(cardPoints) - min_val
            

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

