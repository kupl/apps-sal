def s(l1, l1_start_idx, l2, l2_start_idx):
    if len(l1) < l1_start_idx or len(l2) < l2_start_idx:
        return 0
    
    res = sum(l1[0:l1_start_idx]) + sum(l2[0:l2_start_idx])
    
    l1_end = l1_start_idx + 3 * ((len(l1) - l1_start_idx) // 3)
    res += sum(l1[l1_start_idx:l1_end])
    
    l2_end = l2_start_idx + 3 * ((len(l2) - l2_start_idx) // 3)
    res += sum(l2[l2_start_idx:l2_end])
    
    return res

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        res = 0
        ones = []
        twos = []
        for n in nums:
            mod = n % 3
            if mod == 0:
                res += n
            elif mod == 1:
                ones.append(n)
            elif mod == 2:
                twos.append(n)
        ones.sort(reverse = True)
        twos.sort(reverse = True)
        
        counter = 0
        ones_sum = [0]
        for x in ones:
            counter += x
            ones_sum.append(counter)
        
        counter = 0
        twos_sum = [0]
        for x in twos:
            counter += x
            twos_sum.append(counter)

        m = 0
        for i in range(0, min(len(ones), len(twos)) + 1):
            one_end = i + ((len(ones) - i) // 3 ) * 3
            two_end = i + ((len(twos) - i) // 3 ) * 3
            x = ones_sum[one_end] + twos_sum[two_end]
            m = max(m, x)
        
        res += m
            
        return res
