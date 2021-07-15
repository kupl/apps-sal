class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        # sums = 100 * [0]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    res = nums[i]
                else:
                    res = res + nums[j]
                
                sums.append(res)
                # sums[res] += 1
                
        # for i in range(1, 100):
        #     sums[i] += sums[i-1]
            
        sums = sorted(sums)
        ans = sum(sums[k] for k in range(left-1, right))
        return int(ans % (1e9 + 7))
        
#         i = 0
#         while left < sums[i]:
#             i += 1
#         j = i
#         while right <= sums[j]:
#             j += 1
        
#         ans = i * (sums[i] - (left - 1))
#         for k in range(i, j+1):
#             ans += 
#         return sum(k*sums[k])

