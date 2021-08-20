class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        steps = defaultdict(lambda: None)
        steps[1] = 0
        vals = list(range(lo, hi + 1))
        powers = []
        for v in vals:
            s = v
            num_steps = 0
            while s != 1:
                if steps[s] is not None:
                    num_steps += steps[s]
                    break
                if s % 2 == 0:
                    s //= 2
                else:
                    s = 3 * s + 1
                num_steps += 1
            steps[v] = num_steps
            powers.append(num_steps)
        items = sorted(zip(powers, vals))
        return items[k - 1][1]
