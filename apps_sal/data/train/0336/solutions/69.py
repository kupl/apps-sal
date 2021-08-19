class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # s -> {a: 1, b: 2}
        # t -> {a: 2, b: 1}

        # s -> {f: 1, r: 1, i: 1, e: 1, n: 1, d: 1}
        # t -> {}

        counter = {}
        count = 0

        for c in s:
            counter[c] = counter.get(c, 0) + 1

        for c in t:
            if c in counter and counter[c] > 0:
                counter[c] -= 1
            else:
                count += 1

        return count
