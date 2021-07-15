class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        distance = Counter((ord(b) - ord(a)) % 26 for a, b in zip(s, t) if a != b)
        maxf = [-1, -1]
        for c, f in distance.items():
            if f > maxf[1] or f == maxf[1] and c > maxf[0]:
                maxf[0] = c
                maxf[1] = f
        return not distance or ((maxf[1] - 1) * 26 + maxf[0]) <= k
