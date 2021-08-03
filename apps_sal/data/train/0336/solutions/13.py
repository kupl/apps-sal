class Solution:
    def minSteps(self, s: str, t: str) -> int:
        maps = {}
        mapt = {}
        for i in range(0, len(s)):
            if s[i] not in maps:
                maps[s[i]] = 1
            elif s[i] in maps:
                maps[s[i]] = maps[s[i]] + 1
            if t[i] not in mapt:
                mapt[t[i]] = 1
            elif t[i] in mapt:
                mapt[t[i]] = mapt[t[i]] + 1
        count = 0
        l = set()
        for j in range(0, len(s)):
            if s[j] not in l and s[j] not in mapt:
                l.add(s[j])
                count = count + maps[s[j]]
            elif s[j] not in l and maps[s[j]] > mapt[s[j]]:
                l.add(s[j])
                count = count + (maps[s[j]] - mapt[s[j]])
        return count
