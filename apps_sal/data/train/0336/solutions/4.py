class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_map = {}
        change = 0
        for ch in s:
            if ch not in s_map:
                s_map[ch] = 1
            else:
                s_map[ch] += 1
        for i in range(0, len(t)):
            if t[i] in s_map and s_map[t[i]] > 0:
                s_map[t[i]] -= 1
            else:
                change += 1
        return change
