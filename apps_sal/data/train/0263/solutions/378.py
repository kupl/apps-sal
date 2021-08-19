class Solution:
    valid_jumps = dict()
    valid_jumps[0] = [4, 6]
    valid_jumps[1] = [6, 8]
    valid_jumps[2] = [7, 9]
    valid_jumps[3] = [4, 8]
    valid_jumps[4] = [0, 3, 9]
    valid_jumps[5] = []
    valid_jumps[6] = [0, 1, 7]
    valid_jumps[7] = [2, 6]
    valid_jumps[8] = [1, 3]
    valid_jumps[9] = [2, 4]
    cache = dict()

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        agg = 0
        for idx in range(10):
            if idx != 5:
                agg += self.knightDialerHelper(idx, n - 1)
        return agg % int(1000000000.0 + 7)

    def knightDialerHelper(self, start, n):
        if n == 1:
            return len(self.valid_jumps[start])
        if (start, n) in self.cache.keys():
            return self.cache[start, n]
        numbers = 0
        for k in self.valid_jumps[start]:
            numbers += self.knightDialerHelper(k, n - 1)
        self.cache[start, n] = numbers
        return numbers
