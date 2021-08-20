class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = {format(i, f'0{k}b'): False for i in range(2 ** k)}
        for i in range(len(s) - k + 1):
            ss = s[i:i + k]
            if ss in codes:
                codes[ss] = True
        return all(codes.values())
