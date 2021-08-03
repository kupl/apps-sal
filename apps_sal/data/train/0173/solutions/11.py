'''
现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
如果存在这样的分法，请返回 True ；否则，返回 False 。

思路：首先和得整除。要凑对，那就是mod能凑对，统计mod能否凑对即可
'''


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_count = [0 for i in range(k)]
        for i in arr:
            mod_count[i % k] += 1
        if mod_count[0] % 2:
            return False
        for i in range(1, len(mod_count)):
            if mod_count[i] != mod_count[k - i]:
                return False
        return True
