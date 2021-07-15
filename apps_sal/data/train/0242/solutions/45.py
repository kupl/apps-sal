class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counter = Counter()
        freq_counter = Counter()
        res = 0
        
        for i, num in enumerate(nums):
            if counter[num]:
                freq_counter[counter[num]]-=1
                if not freq_counter[counter[num]]:
                    del freq_counter[counter[num]]
            counter[num] += 1
            freq_counter[counter[num]]+=1
    
            if len(freq_counter)==1:
                for k in freq_counter:
                    if k==1 or freq_counter[k]==1:
                        res = max(res, i+1)
            if len(freq_counter)==2:
                k0, k1 = sorted(freq_counter)
                if freq_counter[1]==1 or k1-k0==1 and freq_counter[k1]==1:
                    res = max(res, i+1)
            # print(i, num, res, freq_counter)
        return res
