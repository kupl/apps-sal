class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
#         我写的还是太复杂了
#         if not cardPoints or not k:
#             return 0
#         if k==len(cardPoints):
#             return sum(cardPoints)
        
#         front={0:0}
#         back={0:0}
#         total=0
#         for i in range(k):
#             total+=cardPoints[i]
#             front[i+1]=total
#         total=0
#         for i in range(-1,-k-1,-1):
#             total+=cardPoints[i]
#             back[-i]=total
            
#         maxres=float('-inf')
#         for i in range(k+1):
#             maxres=max(maxres,front[i]+back[k-i])
        
#         return maxres
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            res = max(res, s)
        return res

