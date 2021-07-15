class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq_count, count, res, maxf = defaultdict(int), defaultdict(int), 0, 0
        
        for i, a in enumerate(nums):
            count[a] += 1
            freq_count[count[a]-1] -= 1
            freq_count[count[a]] += 1
            maxf = max(maxf, count[a])
            if maxf==1 or maxf*freq_count[maxf]+1==i+1 or (maxf-1)*freq_count[maxf-1]+maxf==i+1:
                res = i+1
        
        return res
