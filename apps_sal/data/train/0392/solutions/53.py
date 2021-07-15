from math import comb

class Solution:
    def numWays(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
        if ones == 0:
            return comb(len(s) - 1, 2) % (10**9 + 7)
        
        if ones % 3 != 0:
            return 0
        
        i = 0
        found = 0
        a = None
        while i < len(s):
            c = s[i]
            if c == '1':
                found += 1
            if found == (ones//3):
                count = 0
                i += 1
                c = s[i]
                while c == '0':
                    count += 1
                    i += 1
                    c = s[i]
                if not a:
                    a = count + 1
                    i -= 1
                else:
                    return (a * (count + 1)) % (10**9 + 7)
                found = 0
            i += 1
