from collections import defaultdict
class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         hashmap = defaultdict(int)
#         hashmap[0] = 1
#         accSum, total = 0, 0
#         for n in nums:
#             accSum += 1 if n % 2 ==1 else 0
#             if accSum - k in hashmap:
#                 total += hashmap[accSum - k]
#             hashmap[accSum] += 1
            
#         return total
       def numberOfSubarrays(self, A, k):
            i = count = res = 0
            for j in range(len(A)):
                if A[j] & 1:
                    k -= 1
                    count = 0
                while k == 0:
                    k += A[i] & 1
                    i += 1
                    count += 1
                res += count
            return res
                
    

