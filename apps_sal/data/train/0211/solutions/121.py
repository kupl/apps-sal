class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(s, b):  # split into substrings given bit string b
            res = []
            x, y = s[0], b[0]
            for i in range(1, len(s)):
                if b[i] == y:
                    x += s[i]
                else:
                    res.append(x)
                    x, y = s[i], b[i]
            res.append(x)
            return res

        count = 0
        for i in range(2**(len(s) - 1)):
            b = bin(i)[2:]
            bb = '0' * (len(s) - len(b)) + b    # padding + bits
            res = split(s, bb)
            #print(bb, res)
            if len(res) == len(set(res)):
                count = max(count, len(res))

        return count
