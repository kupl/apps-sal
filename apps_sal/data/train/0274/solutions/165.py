class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_q, min_q = [],[]
        ans = 1
        l = 0
        for i,num in enumerate(nums):
            while len(max_q) and nums[max_q[-1]] < num:
                max_q.pop(-1)
            while len(min_q) and nums[min_q[-1]] > num:
                min_q.pop(-1)
            min_q.append(i)
            max_q.append(i)
            # print(max_q, min_q)
            # max_num = max_q[0]
            # min_num = min_q[0]
            while(nums[max_q[0]]-nums[min_q[0]] > limit):
                if max_q[0] > min_q[0]:
                    l = min_q.pop(0) + 1
                else:
                    l = max_q.pop(0) + 1
            # ans = max(abs(max_q[0]-min_q[0]) +1, ans) 
            ans = max(i-l +1, ans) 
        return ans

