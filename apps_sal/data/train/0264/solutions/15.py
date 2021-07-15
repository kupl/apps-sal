class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def score(s):
            return sum(1 << (ord(c) - ord('a')) for c in s)
        
        def valid(s):
            return collections.Counter(s).most_common()[0][1] <= 1
        arr = [s for s in arr if valid(s)]
        s = [score(s) for s in arr]
        
        res = 0
        for i in range(2**len(s)):
            val = 0
            cur = 0
            for j in range(len(s)):
                if ((1 << j) & i) == 0: continue
                if s[j] & val: break
                val |= s[j]
                cur += len(arr[j])
            else:
                res = max(res, cur)
        return res

