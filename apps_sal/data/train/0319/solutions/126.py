class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dont take the below, because it can be negative, [-1,-2,-3]
        # if len(stoneValue) <= 3:
        #    return 'Alice'
        p1, p2, p3 = 0, 0, 0
        post_sum = 0
        for i in range(len(stoneValue) - 1, -1, -1):
            val = stoneValue[i]
            post_sum += val
            best = post_sum - min([p1, p2, p3])
            p1, p2, p3 = best, p1, p2
        if p1 > post_sum - p1:
            return 'Alice'
        elif p1 < post_sum - p1:
            return 'Bob'
        else:
            return 'Tie'
