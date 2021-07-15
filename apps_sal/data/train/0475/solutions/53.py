# from heapq import heappush, heappop
# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         maxHeap = []
        
#         def maxHeapPush(val):
#             heappush(maxHeap, -val)
#         def maxHeapPop():
#             return -heappop(maxHeap)
#         def maxHeapPeek():
#             return -maxHeap[0]
#         def maxHeapLen():
#             return len(maxHeap)
        
#         for i in range(len(nums)):
#             runningSum = 0
#             for j in range(i, len(nums)):
#                 runningSum += nums[j]
#                 if maxHeapLen() < right:
#                     maxHeapPush(runningSum)
#                 elif maxHeapPeek() > runningSum:
#                     maxHeapPop()
#                     maxHeapPush(runningSum)
                    
#         return sum(maxHeapPop() for _ in range(right - left + 1))%(10**9 + 7)
        
#O(N^2) 
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
            res=[sum(nums[i:j]) for i in range(len(nums)+1) for j in range(i+1, len(nums)+1)]
            # for i in range(len(nums)):
            #     summ = 0
            #     for j in nums[i:]:
            #         summ +=j
            #         res.append(summ)
                
            res.sort()
            return sum(res[left-1:right])%(10**9+7)
        
#O(N^3) 
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        return sum(sorted([sum(nums[i:j]) for i in range(len(nums)+1) for j in range(i+1, len(nums)+1)])[left-1:right])%(10**9+7)
