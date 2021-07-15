class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        pref = [0]
        s = 0
        for i in range(n):
            nums[i] %= p
            s = (s + nums[i]) % p
            pref.append(s)
        if (s == 0): return 0
        target = pref[-1]
        c = dict()
        ans = n
        print(pref)
        for i in range(len(pref)):
            x = (p + pref[i] - target) % p
            if x in c:
                ans = min(ans, i - c[x])
            c[pref[i]] = i
        
        if (ans == n): return -1
        return ans
