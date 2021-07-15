class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # For each i, find j > i, s.t.
        # suf[j] = p - pref[i].
        index = collections.defaultdict(list)
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        for i, x in enumerate(nums):
            pref[i] = (pref[i - 1] + x) % p if i else x % p
        for i in range(n-1,-1,-1):
            suff[i]=(suff[i+1]+nums[i])%p if i<n-1 else nums[i]%p
        suff.append(0)
        for i in range(n,-1,-1):
            index[suff[i]].append(i)
        ans = float('inf')
        if 0 in index and index[0][-1] < n:
            ans = index[0][-1]
        for i in range(n):
            target = (p - pref[i]) % p
            # Find j > i.
            while index[target] and index[target][-1] <= i:
                index[target].pop()
            if index[target]:
                ans = min(ans, index[target][-1] - i - 1)
        return ans if ans < float('inf') else -1
