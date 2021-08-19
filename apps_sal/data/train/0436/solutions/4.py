class Solution:

    def minDays(self, n: int) -> int:

        def t(n):
            stack = {n}
            ct = 0
            while stack:
                tmp = set()
                for i in stack:
                    if i == 0:
                        return ct
                    if i % 2 == 0:
                        tmp.add(i // 2)
                    if i % 3 == 0:
                        tmp.add(i // 3)
                    tmp.add(i - 1)
                ct += 1
                stack = tmp
        return t(n)
