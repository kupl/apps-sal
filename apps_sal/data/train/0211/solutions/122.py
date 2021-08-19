class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        l = len(s)
        for i in range(l - 1, 0, -1):
            for j in itertools.combinations(range(1, l), i):
                cut = [0] + list(j)
                subs = []
                for k in range(len(cut)):
                    if k == len(cut) - 1:
                        subs.append(s[cut[k]:])
                    else:
                        subs.append(s[cut[k]:cut[k + 1]])
                if len(subs) == len(set(subs)):
                    return len(subs)
        return 1
