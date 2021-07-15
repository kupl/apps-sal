class Solution:       
    def lastSubstring(self, s: str) -> str:
        curr_value = 0
        max_value = 0
        max_idx = 0
        char_to_id = {c: i for i, c in enumerate(sorted(set(s)))}
        
        for i in range(len(s) - 1, -1, -1):
            curr_value = char_to_id[s[i]] + curr_value / len(char_to_id)

            if curr_value > max_value:
                max_value = curr_value
                max_idx = i

        return s[max_idx:]
