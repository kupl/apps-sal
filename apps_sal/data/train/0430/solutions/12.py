class Solution:
    def distinctSubseqII(self, S: str) -> int:
        MOD = 10**9 + 7
        
        cur = collections.defaultdict(int)
        for c in S:
            for k in [k for k in cur.keys()]:
                if c!=k:
                    cur[c] += cur[k]
            cur[c] += 1
            cur[c] %= MOD
        
        
        return sum(cur.values()) % MOD
