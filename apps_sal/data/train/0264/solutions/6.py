class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [set(x) for x in arr if len(x) == len(set(x))]
        mx = 0
        
        def util(start, cur):
            nonlocal mx
            if start == len(arr):
                mx = max(mx, len(cur))
            for i in range(start, len(arr)):
                if cur & arr[i]: continue
                cur |= arr[i]
                util(i+1, cur)
                cur ^= arr[i]
            mx = max(mx, len(cur))
        
        util(0, set())
        return mx
