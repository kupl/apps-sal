class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        d = [0]
        
        cumsum = [0]*(n+1)
        for i in range(1,n+1):
            cumsum[i] += (cumsum[i-1]+nums[i-1])
        
        for i in range(n):
            for j in range(i+1, n+1):
                d.append(cumsum[j] - cumsum[i])
        d.sort()
        return sum(d[left:right+1])%(10**9 + 7)

