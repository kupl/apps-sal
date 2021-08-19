class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cnt = Counter([0])
        (pref, ans) = (0, 0)
        for a in A:
            pref = (pref + a) % K
            ans += cnt[pref]
            cnt[pref] += 1
        return ans
