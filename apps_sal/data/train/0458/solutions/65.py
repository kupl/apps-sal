from collections import defaultdict
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        modgrps = defaultdict(lambda: [])
        psums = []
        currsum = 0
        for i in range(n):
            currsum += nums[i]
            modgrps[currsum % p].append(i)
            psums.append(nums[i] + (psums[i-1] if i > 0 else 0))
        tot = currsum
        if tot % p == 0: return 0
        
        qry = lambda i, j: psums[j] if i == 0 else psums[j]-psums[i-1]
        
        ans = float('inf')
        need = tot % p
        for i in range(n):
            curr = psums[i] % p
            x = (curr - need) % p
            if curr == need and i < n-1:
                ans = min(ans, i+1)
            grp = modgrps[x]
            if len(grp) == 0: continue
            index, jump = 0, len(grp)-1
            while jump >= 1:
                while index+jump<len(grp) and grp[index+jump] <= i:
                    index += jump
                jump //= 2
            length = i - (grp[index]+1) + 1
            if length > 0: ans = min(ans, length)
        
        return ans if ans < float('inf') else -1
        
        
        
        
        

