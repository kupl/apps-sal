class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        count = collections.Counter()
        for n in nums:
            if n != 0:
                count[n] += 1
        while len(count) > 0:
            newcount = collections.Counter()
            for k,v in count.items():
                if k%2 == 0:
                    newcount[k//2] += v
                elif k > 1:
                    newcount[(k-1)//2] += v
                    ans += v
                else:
                    ans += v
            ans += 1
                    
            count = newcount
        return ans-1
