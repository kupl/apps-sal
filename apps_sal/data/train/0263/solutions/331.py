jumps = [
    (4, 6),
    (6, 8),
    (7, 9),
    (4, 8),
    (0, 3, 9),
    (),
    (0, 1, 7),
    (2, 6),
    (1, 3),
    (2, 4),
]


class Solution:
    @staticmethod
    def numNumbersFrom(cache, button, ttl):
        if ttl == 0:
            return 0
        if ttl == 1:
            return 1
        if button in cache and ttl in cache[button]:
            return cache[button][ttl]
        total = 0
        for i in jumps[button]:
            total += int(Solution.numNumbersFrom(cache, i, ttl - 1) % (1e9 + 7))
        if button not in cache:
            cache[button] = {}
        cache[button][ttl] = total
        return total

    def knightDialer(self, n: int) -> int:
        total = 0
        cache = {}
        for i in range(0, len(jumps)):
            total += self.numNumbersFrom(cache, i, n)
        return int(total % (1e9 + 7))
