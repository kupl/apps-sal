class Solution:
    def knightDialer(self, n: int) -> int:
        lis = [10, 20, 46, 104, 240, 544]
        if(n <= 6):
            return lis[n - 1]
        for i in range(7, n + 1):
            lis.append(6 * lis[-2] - 4 * lis[-4])
        return lis[-1] % (10**9 + 7)
