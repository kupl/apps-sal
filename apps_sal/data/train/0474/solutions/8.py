from collections import defaultdict as dt


def sc(w, z):
    s = 0
    for i in w:
        s += z[ord(i) - 97]
    return s


def ch(fi, s):
    gi = dt(int)
    for i in s:
        for j in i:
            gi[j] += 1
    for i in gi:
        if gi[i] > fi[i]:
            return False
    return True


class Solution:

    def maxScoreWords(self, x: List[str], y: List[str], z: List[int]) -> int:
        fi = dt(int)
        for i in y:
            fi[i] += 1
        ans = 0
        for j in range(1, len(x) + 1):
            for i in list(combinations(x, j)):
                ss = 0
                if ch(fi, i):
                    for k in i:
                        ss += sc(k, z)
                    ans = max(ss, ans)
        return ans
