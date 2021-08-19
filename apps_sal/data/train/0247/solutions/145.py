class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        d = {}
        d[0] = -1
        possible_sum = {0}
        cur_sum = 0
        for i, a in enumerate(arr):
            cur_sum += a
            possible_sum.add(cur_sum)
            d[cur_sum] = i

        till_len = [float('inf')] * len(arr)
        for s in possible_sum:
            if s + target in possible_sum:
                till_len[d[s + target]] = d[s + target] - d[s]

        ans = float('inf')
        pre_min = [float('inf')] * len(arr)
        for i, t in enumerate(till_len):        # t is the length of good subarrays until index i.
            # if t == float('inf'): continue
            if i == t - 1:
                pre_min[i] = t
            else:
                pre_min[i] = min(t, pre_min[i - 1])
                if t < float('inf') and pre_min[i - t] < float('inf'):
                    ans = min(ans, t + pre_min[i - t])

        return ans if ans < float('inf') else -1
