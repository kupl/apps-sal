class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 1 << (n - 1):
            return ''
        other = [(1, 2), (0, 2), (0, 1)]
        ans = [(k - 1) // (1 << (n - 1))]
        k2bit = bin((k - 1) % (1 << (n - 1)))[2:]
        k2bit = '0' * (n - 1 - len(k2bit)) + k2bit

        for i in range(1, n):
            ans.append(other[ans[i - 1]][int(k2bit[i - 1])])
        letters = 'abc'

        return ''.join([letters[x] for x in ans])
