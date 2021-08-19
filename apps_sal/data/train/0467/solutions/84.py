class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret_count = {}  # N -> Count
        ret_sum = {}  # N -> Sum
        # --
        for n in nums:
            if n in ret_sum:
                if ret_sum[n] is not None:
                    ret_count[n] += 1
                continue
            # calculate it!
            # max_div = int(n ** 0.5)
            # if max_div*max_div >= n:
            #     max_div -= 1  # forbid three
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
            # get result
            if hit_div is not None and hit_div != (n // hit_div):  # hit it!!
                res = 1 + n + hit_div + (n // hit_div)
                ret_count[n] = 1
            else:
                res = None
            ret_sum[n] = res
        # --
        ret = sum(ret_sum[k] * c for k, c in list(ret_count.items()))
        return ret
