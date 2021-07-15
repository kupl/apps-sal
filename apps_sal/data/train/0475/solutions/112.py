import heapq

class Solution:
    def rangeSum(self, nums, n, left, right):
        ans = 0
        array = []
        for i in range(n):
            heapq.heappush(array, (nums[i], i))
        
        count = 1
        while array:
            val, index = heapq.heappop(array)
            if left <= count :
                ans += val
            if index < n-1:
                heapq.heappush(array, (val + nums[index + 1], index+1))
            count += 1
            if count > right:
                break
        return ans % (10**9 + 7)
