class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        def get_in_arry_max_sum():
            cur = 0
            max_val = 0
            for i in range(n):
                cur = max(0, cur) + arr[i]
                max_val = max(max_val, cur)
            return max_val
        
        max_suffix = list(itertools.accumulate(arr))
        max_suffix = [0 if i > 0 and max_suffix[i-1] == 0 else max(0, max_suffix[i]) for i in range(n)]
        max_prefix = list(itertools.accumulate(arr[::-1]))
        max_prefix = [0 if i > 0 and max_prefix[i-1] == 0 else max(0, max_prefix[i]) for i in range(n)][::-1]
        
        mp = max(max_prefix)
        ms = max(max_suffix)
        # print(max_prefix)
        # print(max_suffix)
        in_arry_max_sum = get_in_arry_max_sum()
        if k == 1:
            return in_arry_max_sum
        if k == 2:
            return max(mp + ms, in_arry_max_sum)

        total = sum(arr)
        return max(in_arry_max_sum, mp + ms + (k-2) * max(0, total)) % (10**9+7)
        

