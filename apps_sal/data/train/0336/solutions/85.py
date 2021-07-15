class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # ok try the diff theory but ur tired so it's ok if rn it's wrong
        changes_to_char = {}
        
        for i in range(len(s)):            
            s_char_changes = changes_to_char.get(s[i], 0) + 1
            changes_to_char[s[i]] = s_char_changes
            
            t_char_changes = changes_to_char.get(t[i], 0) - 1
            changes_to_char[t[i]] = t_char_changes

        total_dist = 0
        for char, char_dist in changes_to_char.items():
            if char_dist > 0:
                total_dist += char_dist
        
        # OHH so you only want to outprint the positive values
        # This is because the equilibrium will always be 0 -> i.e. additions of a char
        # means removal of another existing char in s -> as such the number of additions
        # will always equal the number of removals (or else u have a problem with math)
        # But one addition/removal counts as 1 move - so just return number of chantes
        return total_dist
