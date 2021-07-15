class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:  # O(n log n)?
        # dynamic programming / memoization solution?  => wrong!!!
        ## [1, 2, 3, 4] => [[1, 2], [2, 3], [3, 4]]  sum: a + b - 1
        ##                             [[1, 3], [2, 4]] sum: [a, b-1] + [b] - 1  # get midpoint and look-up left and right parts
        ##                                  [[1, 4]] sum: [1:2] + [3:4] -1
        
        ### example: A = [8,1,5,2,6]
        ## memo[dist=1]: [8+1-1=8, 1+5-1=5, 5+2-1=6, 2+6-1=7]
        ## memp[dist=2]: [8+5-1=13]
        # memo = {(i, i): A[i] for i in range(A)}  # (i, j) = sum(i:j)
        # max_score = 0  # max(memo.values())
        # for dist in range(1, len(A)):
        #     for i in range(len(A) - dist):
        #         # get sum
        #         mid = (i + dist) // 2  # for pairs of dist 1 => 0, 1; mid == 0
        #         left_sum = memo[(i, mid)]
        #         right_sum = memo[(mid+1, i+dist)]
        #         memo[(i, i + dist)] = left_sum + right_sum - 1
        #         max_score = max(memo[(i, i + dist)], max_score)  # update max score
        # return max_score
        
        ## idea 2: lagging and leading pointers => calc their score. Move leading on, if score goes down, move lagging next
        lag, lead = 0, 1
        prev_max_score = A[0]
        prev_max_idx = 0
        max_score = 0
        for i in range(1, len(A)):
            score = prev_max_score + A[i] - (i - prev_max_idx)
            max_score = max(score, max_score)
            if A[i] >= score - A[i]:
                prev_max_idx = i
                prev_max_score = A[i]
            
        return max_score

# ex: [100, 1, 1, 1, 1....[1]*_99_, 51, 51, 1, 1, [1]*_99_, 100]

