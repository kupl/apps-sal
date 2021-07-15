class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        cumsum = 0
        last = collections.defaultdict(lambda : -math.inf)
        last[0] = -1
        result = math.inf
        for ind, val in enumerate(nums):
            cumsum += val
            last[cumsum % p] = ind
            result = min(result, ind - last[(cumsum - need) % p])
        if result == math.inf or result == len(nums):
            return -1
        else:
            return result
            
#         length = len(nums)
        
#         suffix_sum = sum(nums)
#         if suffix_sum % p == 0:
#             return 0
#         prefix_sum = 0
#         last = collections.defaultdict(lambda : -math.inf)
#         last[0] = -1
#         result = math.inf
#         for ind, val in enumerate(nums):
#             suffix_sum -= val
#             result = min(result, ind - last[(p - suffix_sum) % p])
#             prefix_sum += val
#             last[prefix_sum % p] = ind
#         if result == math.inf or result == length:
#             return -1
#         else:
#             return result
        
#         prefix = collections.defaultdict(list)
#         prefix[0].append(-1)
#         now = 0
#         for ind, val in enumerate(nums):
#             now += val
#             prefix[now % p].append(ind)
            
#         suffix = collections.defaultdict(collections.deque)
#         suffix[0].appendleft(len(nums))
#         now = 0
#         for ind, val in list(enumerate(nums))[::-1]:
#             now += val
#             suffix[now % p].appendleft(ind)
            
#         result = math.inf
#         if suffix[0] and suffix[0][0] != len(nums):
#             result = suffix[0][0]
#         now = 0
#         for ind, val in enumerate(nums):
#             now += val
#             rights = suffix[(p - (now % p)) % p]
#             right = bisect.bisect(rights, ind)
#             if right < len(rights):
#                 result = min(result, rights[right] - ind - 1)
        
#         if result == math.inf:
#             return -1
#         else:
#             return result
        
        
#         all_sum = sum(nums)
        
#         presum = itertools.accumulate(nums) + [0]
#         lo = 0
#         hi = len(nums)
#         result = -1
#         while lo < hi:
#             mid = (lo + hi) // 2
#             for i in range(len(nums) - mid + 1):
#                 if ((all_sum - (presum[i + mid - 1] - presum[i - 1])) / p) % 1 == 0:
#                     result = mid
#                     hi = mid
#                 else:

