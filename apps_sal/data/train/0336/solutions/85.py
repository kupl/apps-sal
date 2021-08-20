class Solution:

    def minSteps(self, s: str, t: str) -> int:
        changes_to_char = {}
        for i in range(len(s)):
            s_char_changes = changes_to_char.get(s[i], 0) + 1
            changes_to_char[s[i]] = s_char_changes
            t_char_changes = changes_to_char.get(t[i], 0) - 1
            changes_to_char[t[i]] = t_char_changes
        total_dist = 0
        for (char, char_dist) in changes_to_char.items():
            if char_dist > 0:
                total_dist += char_dist
        return total_dist
