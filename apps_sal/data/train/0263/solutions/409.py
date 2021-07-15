MAX = 10**9 + 7

d = {
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
    0: [4, 6]
}

class Solution:
    def __init__(self):
        self.memo = {}
    
    def knightDialer(self, n: int) -> int:
        return sum([self.helper(n, p) for p in d.keys()]) % MAX
    
    def helper(self, n: int, p: int) -> int:
        if (n, p) in self.memo: return self.memo[(n, p)]
        if n == 1: return 1
        r = sum([self.helper(n - 1, q) for q in d[p]])
        self.memo[(n, p)] = r
        return r
