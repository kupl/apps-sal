class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        freqs = [f + 1 for f in Counter(tiles).values()]
        for t in itertools.product(*map(range, freqs)):
            n = sum(t)
            subtotal = math.factorial(n)
            for freq in t:
                subtotal //= math.factorial(freq)
            res += subtotal
        return res - 1
