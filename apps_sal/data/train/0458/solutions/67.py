class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        目标是找到一个子串的余数为r
        到当前位置所有数和的余数减去r对应的余数位置，中间就是余数为r的子串
        Calculate the need = sum(A) % p.
Then one pass, record the prefix sum in a hashmap.

Then the question become:
Find the shortest array with sum % p = need.

last[remainder] = index records the last index that
(A[0] + A[1] + .. + A[i]) % p = remainder
        """
        r = sum(nums) % p
        if r == 0:
            return 0
        mem = {0: -1}
        s = 0
        res = len(nums)
        for (i, a) in enumerate(nums):
            s = (s + a) % p
            t = (s + p - r) % p
            if t in mem:
                res = min(res, i - mem[t])
            mem[s] = i
        if res == len(nums):
            return -1
        return res
