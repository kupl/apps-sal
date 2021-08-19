class Solution:

    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        (maxC, N) = (max(s), len(s))
        inds = [i for i in range(N) if s[i] == maxC and (i == 0 or s[i - 1] != maxC)]
        maxind = inds[0]
        for i in range(1, len(inds)):
            cur_sub_start = inds[i]
            pointer = 0
            while cur_sub_start + pointer < N:
                if s[cur_sub_start + pointer] > s[maxind + pointer]:
                    maxind = inds[i]
                    break
                elif s[cur_sub_start + pointer] == s[maxind + pointer]:
                    pointer += 1
                else:
                    break
        return s[maxind:]
