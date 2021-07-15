class Solution:
    def numSub(self, s: str) -> int:
        result, stop_idx = 0, -1
        for idx, char in enumerate(s):
            if char != '1' or idx <= stop_idx:
                continue
            
            freq = 1
            next_idx = idx + 1
            while (next_idx < len(s) and s[next_idx] == '1'):
                freq += 1
                stop_idx = next_idx
                next_idx += 1
            
            result += (freq + 1)*freq/2
        
        return int(result % (1e9 + 7))

