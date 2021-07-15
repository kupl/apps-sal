class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = [0]*(len(nums)+1)
        for i,n in enumerate(nums):
            l[i+1]=l[i]+n%2
        c = Counter(l)
        #print(l)
        return sum(c[x-k]*c[x] for x in c)

