class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = {}
        def f(i, run_ch, run_len, remain_dels):
            if i == len(s):
                return 0
            key = (i, run_ch, run_len, remain_dels)
            if key in memo:
                return memo[key]
            del_costs = float('inf')
            if remain_dels > 0:
                del_costs = f(i+1, run_ch, run_len, remain_dels-1)
            
            keep_costs = 0
            if s[i] == run_ch:
                extra_cost = 0
                if run_len == 1 or len(str(run_len+1)) > len(str(run_len)):
                    extra_cost = 1
                keep_costs = extra_cost + f(i+1, run_ch, run_len+1, remain_dels)
            else:
                keep_costs = 1 + f(i+1, s[i], 1, remain_dels)
            
            memo[key] = min(del_costs, keep_costs)
            return memo[key]
        return f(0, '', 0, k)

