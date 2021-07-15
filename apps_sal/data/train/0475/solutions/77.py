class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pre = 0
        sums = [0]
        for el in nums:
            pre += el
            sums.append(pre)
            
        sorted_sums = sorted([ sums[j]-sums[i] for i in range(n+1) for j in range(i+1, n+1) ])
        return sum(sorted_sums[left-1:right]) % (10**9 + 7)
                

