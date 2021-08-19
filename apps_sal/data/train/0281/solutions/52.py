class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        m = len(t)
        if m != n:
            return False
        if s == t:
            return True
        shift = {}
        shift[0] = 0
        for i in range(n):
            move = (ord(t[i]) - ord(s[i])) % 26
            if move > 0:
                if move in shift:
                    new_move = 26 * shift[move] + move
                    shift[move] = shift[move] + 1
                    move = new_move
                else:
                    shift[move] = 1
                if move > k:
                    return False
            else:
                shift[0] = shift[0] + 1
        return True
