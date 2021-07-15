class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sum = list(accumulate(arr))
        suffix_sum = list(accumulate(arr[::-1]))
        
        def helper(prefix_sum, n, target):
            dict_x = {0:-1}
            l_1 = [n+1 for _ in range(n)]
            for i in range(n):
                t1 = prefix_sum[i]-target
                x = n+1
                if dict_x.get(t1, 'x') != 'x':
                    x = i-dict_x[t1]
                l_1[i] = min(x, l_1[i-1] if i > 0 else n+1)
                dict_x[prefix_sum[i]] = i
            return l_1
        
        l = helper(prefix_sum, n, target)
        r = helper(suffix_sum, n, target)[::-1]
        
        ans = sys.maxsize
        for i in range(n-1):
            ans = min(ans, l[i]+r[i+1])
        print(ans)
        return ans if ans <= n else -1
                

