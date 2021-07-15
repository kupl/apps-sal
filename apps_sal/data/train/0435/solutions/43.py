class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # use the prefix sum 
        prefix = [0]
        for a in A:
            prefix += [(prefix[-1] + a) % K]
        #count how many of them are the same
        cnt = collections.Counter(prefix)
        # for the index with the same remainder, randomly choose pairs
        return int(sum( v * (v-1) / 2 for v in list(cnt.values())))

