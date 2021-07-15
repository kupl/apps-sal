class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
#         dq = deque()
#         #dq[i] = number of sequences with i elements, ending with current number
#         c = Counter(nums)
#         nums = sorted(set(nums))
#         current_num = 0
#         opening = 0
#         for i in range(len(nums)):
#             if i > 0 and nums[i] > nums[i - 1] + 1 and opening > 0:
#                 return False
#             if c[nums[i]] < opening:
#                 return False
#             dq.appendleft(c[nums[i]] - opening)
#             opening += c[nums[i]] - opening
#             if len(dq) >= k:
#                 opening -= dq.pop()
#         return opening == 0

        c = Counter(nums)
        nums = list(set(nums))
        heapify(nums)
        # print(list(set(nums)))
        print(nums)
        while nums:
            m = heappop(nums)
            while nums and c[m] == 0:
                m = heappop(nums)
            for i in range(1, k):
                if c[m + i] < c[m]:
                    print((c[m + i], c[m], m))
                    return False
                c[m + i] -= c[m]
            c[m] = 0
        return True
                    
            
                    
                
            

