'''
what would be the state ? 
i: current position 
partition start 

just try allof them is probably the answer

[1,15,7,9,2,5,10]

try all possible partitions and keep track of the max and sum so far 


helper(start, i)

    for j in range(i, k - i + start + 1): 
        helper(start, j)
    
    
if i = 2 and start = 1 and k = 3
from i=2 to 5 - 1 = 4
instead it should be 1, 2, 3, so only one more so i + 1 = i + k - i 

if i = 2 and start = 1 and k = 4
it shld be 1, 2, 3, 4

i just want to know much left to get to k 
k = end - start 
k = j + i - start -> j = k - i + start

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def helper(i, left, curr_max, sum_so_far):
            print(\"helper i =\", i, \", left =\", left, \", curr_max =\", curr_max)
            
            if i == len(arr):
                self.res = max(self.res, sum_so_far + (curr_max * (k - left)))
                return 0
            
            choice1 = float('-inf')
            if left > 0:
                choice1 = helper(i + 1, left - 1, max(curr_max, arr[i]), sum_so_far)
            
            choice2 = helper(i + 1, k, arr[i], sum_so_far + (curr_max * (k - left)))
            
            print(\"choice1 =\", choice1, \", choice2 =\", choice2)
            return max(choice1, choice2)
            
        self.res = float('-inf')
        helper(0, k, arr[0], 0)
        return self.res
'''

'''
dp[i]: max sum for arr ending at i 
'''


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], K: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n + 1)]
        for i in range(n):
            currMax = 0
            for k in range(1, min(K, i + 1) + 1):
                currMax = max(currMax, arr[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + (currMax * k))
        return dp[n - 1]
