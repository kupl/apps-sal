class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        (frogs, c, r, o, a, k) = (0, 0, 0, 0, 0, 0)
        for char in croakOfFrogs:
            if char == 'c':
                c += 1
                frogs = max(frogs, c - k)
            elif char == 'r':
                r += 1
            elif char == 'o':
                o += 1
            elif char == 'a':
                a += 1
            elif char == 'k':
                k += 1
            else:
                return -1
            if not c >= r >= o >= a >= k:
                return -1
        if c == k:
            return frogs
        return -1
