class Solution:

    def minDays(self, n: int) -> int:
        step = 0
        tries = set([n])
        while len(tries) > 0:
            nt = set()
            step += 1
            for t in tries:
                if t == 1:
                    return step
                if t % 2 == 0:
                    nt.add(t // 2)
                if t % 3 == 0:
                    nt.add(t // 3)
                nt.add(t - 1)
            tries = nt
        return -1
