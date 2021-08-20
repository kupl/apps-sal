from collections import defaultdict


class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        s = defaultdict(int)
        for a in A:
            if a <= 0:
                if 2 * a in s:
                    s[2 * a] -= 1
                    if not s[2 * a]:
                        del s[2 * a]
                else:
                    s[a] += 1
            elif a % 2 == 0 and a // 2 in s:
                s[a // 2] -= 1
                if not s[a // 2]:
                    del s[a // 2]
            else:
                s[a] += 1
        return not s
