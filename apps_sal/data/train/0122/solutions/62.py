class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre_sum = []   # i: sum of all items before i
        temp_left = 0
        for i, v in enumerate(cardPoints):
            pre_sum.append(temp_left)
            temp_left += v
        pre_sum.append(temp_left)
        
        post_sum = []  # i: sum of all items after i-1
        temp_right = 0
        temp_right = 0
        for i in range(len(cardPoints)-1, -1, -1):
            v = cardPoints[i]
            post_sum.append(temp_right)
            temp_right += v
        post_sum.append(v)
        post_sum.reverse()
        # print(pre_sum)
        # print(post_sum)
        return max([pre_sum[i] + post_sum[-(k-i)-1] for i in range(k+1)])
            
            
            


