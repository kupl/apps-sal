class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = dict()
        t_count = dict()
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1

        sim_count = 0
        for key in list(s_count.keys()):
            if t_count.get(key, 0):
                if s_count[key] >= t_count[key]:
                    sim_count += t_count[key]
                else:
                    sim_count += s_count[key]
        return len(s) - sim_count
