class Solution:
    def minDays(self, n: int) -> int:
        s = {n}
        step = 0
        while s:
            ns = set()
            for curr in s:
                if curr == 0:
                    return step
                if curr - 1 not in s:
                    ns.add(curr - 1)
                if curr % 2 == 0 and curr // 2 not in s:
                    ns.add(curr // 2)
                if curr % 3 == 0 and curr // 3 not in s:
                    ns.add(curr // 3)
            step += 1
            s = ns
        return step
