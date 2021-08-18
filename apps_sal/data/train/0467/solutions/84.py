class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret_count = {}
        ret_sum = {}
        for n in nums:
            if n in ret_sum:
                if ret_sum[n] is not None:
                    ret_count[n] += 1
                continue
            cur_div = 2
            hit_div = None
            while cur_div * cur_div <= n:
                if n % cur_div == 0:
                    if hit_div is None:
                        hit_div = cur_div
                    else:
                        hit_div = None
                        break
                cur_div += 1
            if hit_div is not None and hit_div != (n // hit_div):
                res = 1 + n + hit_div + (n // hit_div)
                ret_count[n] = 1
            else:
                res = None
            ret_sum[n] = res
        ret = sum(ret_sum[k] * c for k, c in list(ret_count.items()))
        return ret
