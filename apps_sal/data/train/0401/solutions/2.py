
# 1262. Greatest Sum Divisible by Three

# Explanation: seen[i] means the current maximum possible sum that sum % 3 = i
# Complexity: Time O(N), Space O(1)

class Solution1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for a in nums:
            for i in seen[:]: # 这里必须用 [:] 否则 下一次迭代会使用更新后的值 计算结果不对
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
                # print(a, i, seen)
        return seen[0]
    
# Divide the whole list into three parts: mod_0, mod_1, mod_2.
# Think about the sum of the original list, if it mods 3 == 0, then we can just return the sum.
# If tot_sum % 3 == 1, then we should remove one smallest element from mod_1 or two smallest ones from mod_2.
# If tot_sum % 3 == 2, then we should remove one smallest element from mod_2 or two smallest ones from mod_1.

class Solution: # （没明白。。）
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod_1, mod_2,res,remove = [], [], 0, float('inf')
        for i in nums:
            if i % 3 == 0: res += i
            if i % 3 == 1: mod_1 += [i]
            if i % 3 == 2: mod_2 += [i]
        mod_1.sort(reverse = True)
        mod_2.sort(reverse = True)
        tmp = sum(mod_1) + sum(mod_2)
        if tmp % 3 == 0:
            return res + tmp
        elif tmp% 3 == 1:
            if len(mod_1): 
                remove = min(remove, mod_1[-1])
            if len(mod_2) > 1: 
                remove = min(mod_2[-1] + mod_2[-2], remove)
        elif tmp % 3 == 2:
            if len(mod_2): 
                remove = min(remove, mod_2[-1])
            if len(mod_1) > 1: 
                remove = min(mod_1[-1] + mod_1[-2], remove)
        return res + tmp - remove
