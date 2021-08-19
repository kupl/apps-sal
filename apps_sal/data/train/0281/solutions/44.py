class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnts = [0] * 26
        for (s_char, t_char) in zip(s, t):
            if s_char == t_char:
                continue
            elif s_char > t_char:
                moves_req = 26 - (ord(s_char) - ord(t_char))
            else:
                moves_req = ord(t_char) - ord(s_char)
            cnts[moves_req] += 1
            if moves_req > k or cnts[moves_req] > (k - moves_req) // 26 + 1:
                return False
        return True
