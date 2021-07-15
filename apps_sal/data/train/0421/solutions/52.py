class Solution:
    def lastSubstring(self, s: str) -> str:
        lastc = max(s)
        n = len(s)
        q = [i for i,val in enumerate(s) if val==lastc]
        if len(q) == len(s):
            return s
        res = s[q[0]]
        while q:
            qq = []
            for i in q:
                if i+1 < n:
                    qq += [i+1]
            if not qq:
                break
            c = max(s[i] for i in qq)
            res += c
            q = [i for i in qq if s[i] == c]
        
        return res
    # def lastSubstring(self, s: str) -> str:
    # \tS, L, a = [ord(i) for i in s] + [0], len(s), 1
    # \tM = max(S)
    # \tI = [i for i in range(L) if S[i] == M]
    # \tif len(I) == L: return s
    # \twhile len(I) != 1:
    # \t\tb = [S[i + a] for i in I]
    # \t\tM, a = max(b), a + 1
    # \t\tI = [I[i] for i, j in enumerate(b) if j == M]
    # \treturn s[I[0]:]
        
        #ans = [s[i:] for i in lead]
        # print(ans)
        # start = s.index(lastc)
        # while s[start]:
        #     print(start)
        #     ans.append(s[start:])
        #     print(ans)
        #     if s[start+1:].count(lastc) == 0:
        #         break
        #     else:
        #         start += s[start+1:].index(lastc) + 1
        # print(ans)
        return sorted(ans)[-1]

