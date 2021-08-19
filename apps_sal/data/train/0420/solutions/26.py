class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        mask = '00000'
        table = dict()
        table[mask] = -1
        vowels = 'aeiou'
        res = 0
        for (i, c) in enumerate(s):
            for j in range(5):
                if c == vowels[j]:
                    mask1 = list(mask)
                    mask1[j] = str(1 - int(mask1[j]))
                    mask = ''.join(mask1)
            pre_idx = table.get(mask, -2)
            if pre_idx != -2:
                res = max(res, i - pre_idx)
            else:
                table[mask] = i
        return res
