class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        c = collections.defaultdict(int)
        s = 0
        c[0] += 1
        res = 0
        mod = 10 ** 9 + 7
        for x in arr:
            s ^= x%2
            res += c[1-s]
            res %= mod
            c[s] += 1
        return res

