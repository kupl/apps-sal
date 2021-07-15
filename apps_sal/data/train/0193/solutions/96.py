class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = collections.defaultdict(int)
        for i in arr:
            d[i] += 1
        s = sorted([(d[i],i) for i in d],reverse=True)
        res = 0
        ans = 0
        for i,v in s:
            res += i
            ans += 1
            if res >= (len(arr) + 1) // 2: return ans
        return len(d)
