import collections
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        cache=collections.Counter({0:1})
        currentSum=0
        count=0
        for num in A:
            currentSum+=num
            count+=cache[currentSum-S]
            cache[currentSum]+=1
        return count
