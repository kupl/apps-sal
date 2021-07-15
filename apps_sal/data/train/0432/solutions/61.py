import collections
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count=collections.Counter(nums)
        sorted_keys=sorted(count.keys())
        while sorted_keys:
            key=sorted_keys.pop(0)
            val=count[key]
            if val>0:
                for i in range(key,key+k):
                    count[i]-=val
                    if count[i]<0:
                        return False
        return True
                

