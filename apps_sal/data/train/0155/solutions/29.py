class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        '''
        [6,4,14,6,8,13,9,7,10,6,12], d = 2
        dp(i) = 1 + 
        max{
        within i-d <j< i+d
        not arr[k] > arr[i] between i, j
        }
        res = 0
        j from i-1 to i-d (0<=j<len(arr)), while arr[j]<arr[i]: res = max(res, recurse j) 
        i+1 to i+d
        memo
        return res + 1

        '''
        max_pos = 1
        memo = {}

        def helper(i):
            if i in list(memo.keys()):
                return memo[i]
            res = 0
            j = i - 1
            while 0 <= j < len(arr) and i - j <= d and arr[j] < arr[i]:
                res = max(res, helper(j))
                j -= 1
            j = i + 1
            while 0 <= j < len(arr) and j - i <= d and arr[j] < arr[i]:
                res = max(res, helper(j))
                j += 1
            res = res + 1
            memo[i] = res
            return res

        for i in range(len(arr)):
            max_pos = max(max_pos, helper(i))
        return max_pos
