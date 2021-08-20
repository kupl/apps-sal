class Solution:

    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        src = Counter(s)
        des = Counter(t)
        src.subtract(des)
        freq = list(src.values())
        ans = 0
        freq = sorted(freq)
        freq = list([a for a in freq if a != 0])
        while len(freq) > 1:
            actions = min(abs(freq[0]), freq[-1])
            ans += actions
            freq[0] = actions + freq[0]
            freq[-1] = freq[-1] - actions
            freq = list([a for a in freq if a != 0])
        if len(freq) == 1:
            ans += freq[0]
        return ans
