class Solution:

    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1
        obj = dict()
        missing = dict()
        total = 0
        for i in range(len(s)):
            if obj.get(s[i]) == None:
                obj[s[i]] = 1
            else:
                obj[s[i]] = obj[s[i]] + 1
        for j in range(len(t)):
            if obj.get(t[j]) == None:
                if missing.get(t[j]) == None:
                    missing[t[j]] = 1
                else:
                    missing[t[j]] = missing[t[j]] + 1
            elif obj.get(t[j]) == 1:
                del obj[t[j]]
            else:
                obj[t[j]] = obj[t[j]] - 1
        for key in missing.keys():
            total = total + missing.get(key)
        return total
