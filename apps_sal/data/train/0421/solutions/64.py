class Solution:

    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        (maxC, N) = (max(s), len(s))
        inds = [i for i in range(N) if s[i] == maxC and (i == 0 or s[i - 1] != maxC)]
        print(inds)
        maxind = inds[0]
        for i in range(1, len(inds)):
            curind = inds[i]
            step = 0
            while curind + step < N:
                if s[curind + step] > s[maxind + step]:
                    maxind = curind
                    break
                elif s[curind + step] == s[maxind + step]:
                    step += 1
                else:
                    break
        return s[maxind:]
