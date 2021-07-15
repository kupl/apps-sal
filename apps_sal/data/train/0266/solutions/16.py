class Solution:
    def numSplits(self, s: str) -> int:
        
        good_splits = 0
        first_map = {}
        s_map = {}
        
        for letter in s:
            if s_map.get(letter):
                s_map[letter] += 1
            else:
                s_map[letter] = 1
                
        for split_point in range(len(s)):
            if first_map.get(s[split_point]):
                first_map[s[split_point]] = first_map[s[split_point]] + 1
            else:
                first_map[s[split_point]] = 1
            s_map[s[split_point]] = s_map[s[split_point]] - 1
            f_keys = [k for k,v in list(first_map.items()) if v > 0]
            s_keys = [k for k,v in list(s_map.items()) if v > 0]
            if len(f_keys) == len(s_keys):
                good_splits += 1
                
        return good_splits

