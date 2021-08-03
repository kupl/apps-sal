class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        N = 3 << (n - 1)
        res = ''
        if k > N:
            return res
        k -= 1
        letters = ('a', 'b', 'c')
        res += letters[k * 3 // N]
        N //= 3
        k %= N
        for i in range(1, n):
            prev = res[i - 1]
            index = k * 2 // N
            offset = int(prev <= letters[index])
            res += letters[index + offset]
            N >>= 1
            k %= N
        return res
