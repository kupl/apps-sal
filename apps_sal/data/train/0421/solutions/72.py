class Solution:
    def lastSubstring(self, s: str) -> str:
        ls = max(set(s))
        best_symbol = s.index(ls)
        first_symbol = best_symbol
        f = first_symbol
        while s[best_symbol] in s[first_symbol + 1:]:
            next_symbol = s.index(s[best_symbol], first_symbol + 1)
            next_symbol_ = next_symbol
            f_ = f
            while next_symbol_ < len(s) and s[f_] == s[next_symbol_]:
                f_ += 1
                next_symbol_ += 1

            if next_symbol_ < len(s) and s[f_] < s[next_symbol_]:
                f = next_symbol
            elif next_symbol_ == len(s):
                break
            first_symbol = next_symbol
        return s[f:]
