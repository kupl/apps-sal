class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s) != len(t):
            return False
        
        cnts = [0]*26
        for char_s, char_t in zip(s, t):
            if char_s == char_t:
                continue
            elif char_s < char_t:
                moves_req = ord(char_t) - ord(char_s)
            else:
                moves_req = 26 - ord(char_s) + ord(char_t)
                
            cnts[moves_req] += 1
            if moves_req > k or cnts[moves_req]-1 > ((k-moves_req)/26):
                return False
        return True
            

