class Solution:
    def minSteps(self, s: str, t: str) -> int:

        tt = Counter(t)
        ss = Counter(s)

        cnt = 0
        all_c = set(s + t)

        for k in all_c:
            if tt[k] < ss[k]:
                cnt += ss[k] - tt[k]

        return cnt
