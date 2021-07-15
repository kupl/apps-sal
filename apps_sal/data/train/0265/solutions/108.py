class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         prefix = [0] * (n + 1)
#         idx = []
#         for i in range(1, n + 1):
#             prefix[i] = prefix[i - 1] + nums[i - 1]
#         for i in range(n + 1):
#             for j in range(i + 1, n + 1):
#                 if prefix[j] - prefix[i] == target:
#                     idx.append([i, j])
#                     break

#         self.ans = 0        
#         def backtrk(cur, start):
#             if start == len(idx):
#                 self.ans = max(self.ans, len(cur))
#                 return
#             visited = set()
#             for i in range(start, len(idx)):
#                 if len(cur) >= 1 and idx[i][0] < cur[-1][1]:
#                     continue
#                 x, y = idx[i][0], idx[i][1]   
#                 backtrk(cur + [(x, y)], i + 1)
#         backtrk([], 0)
#         return self.ans
               
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1]+x)
        res = 0 
        seen = set()
        for x in prefix:
            if x-target in seen:
                res += 1
                seen = {x}
            else:
                seen.add(x)
        return res
