class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set((format(i, f'0{k}b') for i in range(2 ** k)))
        found = [False for i in range(2 ** k)]
        for i in range(len(s) - k + 1):
            if s[i:i + k] in codes:
                found[int(s[i:i + k], base=2)] = True
        return all(found)
