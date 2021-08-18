class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        t_counter = Counter(t)
        changes = 0

        for key in list(s_counter.keys()):
            changes += abs(s_counter[key] - t_counter[key])

        for key in list(t_counter.keys()):
            changes += 0 if key in s_counter else t_counter[key]

        return changes // 2
