class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        mod_count = Counter({0:1})
        
        ans = 0
        for s in [*accumulate(A)]:
            m = s % K
            if m in mod_count:
                ans += mod_count[m]
            mod_count[m] += 1
        return ans
