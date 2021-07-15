class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = {}
        freq_t = {}

        for keys in s:
            freq_s[keys] = freq_s.get(keys, 0) + 1
        
        for t_keys in t:
            freq_t[t_keys] = freq_t.get(t_keys, 0) + 1
        
        changes = 0
        for key, val in freq_s.items():
            val = freq_s[key]
            val_t = freq_t.get(key, 0)
            
            if val > val_t:
                changes += val - val_t 
        
        return changes
