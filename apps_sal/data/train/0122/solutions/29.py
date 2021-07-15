class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        front = [0] * k
        back = [0] * k
        front[0] = cardPoints[0]
        for i in range(1,k):
            front[i] = front[i-1] + cardPoints[i]
            
        back[0] = cardPoints[-1]
        for i in range(1,k):
            back[i] = back[i-1] + cardPoints[-1-i]
        
        max_score = 0
        print(front,back)
        for i in range(k+1):
            if i == 0:
                max_score = max(max_score,back[-1])
                # print(i,back[-1])
            elif i == k:
                max_score = max(max_score,front[k-1])
                # print(i,front[k-1])
            else:
                max_score = max(max_score,front[i-1]+back[k-i-1])
                # print(i,k-i,max_score,front[i-1]+back[k-i-1])
            # print(i,k-i,max_score)
        return max_score
