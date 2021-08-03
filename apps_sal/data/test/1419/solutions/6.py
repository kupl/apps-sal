import re


class Solution(object):
    def minWidth(self):
        k = int(input())
        s = input()
        words = re.split(' |-', s)
        l = []
        for i in range(len(words)):
            l.append(len(words[i]) + 1)
        l[-1] -= 1
        start = max(sum(l) // k, max(l)) - 1
        end = max(l) + sum(l) // k + 1

        def can(pos):
            c = 1
            cur = 0
            for i in range(len(l)):
                cur += l[i]
                if cur > pos:
                    c += 1
                    cur = l[i]
                    if c > k:
                        return False
            return True
        while (end - start > 1):
            pos = (start + end) // 2
            if can(pos):
                end = pos
            else:
                start = pos
        print(end)


sol = Solution()
sol.minWidth()
