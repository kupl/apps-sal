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
                # if cands[i][0]+1 < len(s) and s[cands[i][0]+1] == max_char:
                #    if i>0 and cands[i-1][0]+1 < cands[i][1]:
                #        continue
                #    new_cands.append((cands[i][0]+1, cands[i][1]))
            '''
            skip = False
            for i in range(len(cands)):
                if cands[i][0]+1 < len(s) and s[cands[i][0]+1] == max_char:
                    if skip == True:
                        skip = False
                        continue
                    if i>len(cands)-1 and cands[i][0]+1 >= cands[i+1][1]:
                        skip = True
                    new_cands.append((cands[i][0]+1, cands[i][1]))
            '''
            cands = new_cands

        return s[cands[0][1]:]
