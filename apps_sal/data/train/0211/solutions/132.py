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
            # print(res)
            return res

        max_len = 0
        for i in range(2**(len(s) - 1)):
            b = bin(i)[2:]
            b = '0' * (len(s) - len(b)) + b
            res = split(s, b)  # split based on bit string
            if len(res) == len(set(res)):  # check if the split forms valid substrings
                max_len = max(max_len, len(res))  # compare against max length so far
        return max_len
