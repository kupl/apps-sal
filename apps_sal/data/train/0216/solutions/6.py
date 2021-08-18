class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        chr_c, chr_r, chr_o, chr_a = 0, 0, 0, 0
        count = 0
        for s in croakOfFrogs:
            if s == 'c':
                chr_c += 1
            elif s == 'r':
                if chr_c <= 0:
                    return -1
                chr_c -= 1
                chr_r += 1
            elif s == 'o':
                if chr_r <= 0:
                    return -1
                chr_r -= 1
                chr_o += 1
            elif s == 'a':
                if chr_o <= 0:
                    return -1
                chr_o -= 1
                chr_a += 1
            else:
                if chr_a <= 0:
                    return -1
                chr_a -= 1
            count = max(count, chr_c + chr_r + chr_o + chr_a)
        if chr_c + chr_r + chr_o + chr_a > 0:
            return -1
        return count
