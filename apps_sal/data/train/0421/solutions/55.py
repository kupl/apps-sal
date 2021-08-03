class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        # get max char from s
        maxC, N = max(s), len(s)
        # get max char indexs to append into inds
        # only store the first ind for consecutive max chars
        inds = [i for i in range(N) if s[i] == maxC and (i == 0 or s[i - 1] != maxC)]
        maxind = inds[0]  # starting index of the max substring

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
