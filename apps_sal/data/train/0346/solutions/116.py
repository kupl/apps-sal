class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cache=collections.Counter({0:1})
        res,cnt_odd=0,0
        for i in range(len(nums)):
            if nums[i]%2==1:
                cnt_odd+=1
            res+=cache.get(cnt_odd-k,0)
            cache[cnt_odd]+=1
        return res

