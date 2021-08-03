class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        diff = [(ord(c2) - ord(c1)) % 26 for c1, c2 in zip(s, t)]
        ctr = sorted((v, k) for k, v in list(collections.Counter(diff).items()) if k)
        return not ctr or (ctr[-1][0] - 1) * 26 + ctr[-1][1] <= k
