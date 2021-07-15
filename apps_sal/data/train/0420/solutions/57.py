class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bin_map = collections.defaultdict(int)
        
        for (i, c) in enumerate(['a', 'e', 'i', 'o', 'u']):
            bin_map[c] = 1 << i
            
        cur_bin = 0
        prev_bin = {0: -1}
        ans = 0
        
        
        for (index, c) in enumerate(s):
            
            cur_bin ^= bin_map[c]
            
            if cur_bin in prev_bin:
                ans = max(ans, index - prev_bin[cur_bin])
            else:
                prev_bin[cur_bin] = index
        return ans
            
            

