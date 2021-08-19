class Solution:

    def lastSubstring(self, s: str) -> str:
        max_char = s[0]
        for i in range(len(s)):
            if s[i] > max_char:
                max_char = s[i]
        cands = []
        for i in range(len(s)):
            if s[i] == max_char:
                cands.append((i + 1, i))
        while len(cands) > 1:
            new_cands = []
            max_char = s[cands[0][0]]
            for i in range(len(cands)):
                if cands[i][0] < len(s) and s[cands[i][0]] > max_char:
                    max_char = s[cands[i][0]]
            i = 0
            while i < len(cands):
                if cands[i][0] < len(s) and s[cands[i][0]] == max_char:
                    new_cands.append((cands[i][0] + 1, cands[i][1]))
                if i < len(cands) - 1 and cands[i][0] == cands[i + 1][1]:
                    i += 2
                else:
                    i += 1
            '\n            skip = False\n            for i in range(len(cands)):\n                if cands[i][0]+1 < len(s) and s[cands[i][0]+1] == max_char:\n                    if skip == True:\n                        skip = False\n                        continue\n                    if i>len(cands)-1 and cands[i][0]+1 >= cands[i+1][1]:\n                        skip = True\n                    new_cands.append((cands[i][0]+1, cands[i][1]))\n            '
            cands = new_cands
        return s[cands[0][1]:]
