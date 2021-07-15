class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        i, j, k = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        maxL = max(len(i), len(j), len(k))
        i, j, k = '0' * (maxL - len(i)) + i, '0' * (maxL - len(j)) + j, '0' * (maxL - len(k)) + k
        cnt = 0
        for x, y, z in zip(i, j, k):
            if z == '1' and x == '0' and y == '0':
                cnt += 1
            if z == '0':
                if x == '1':
                    cnt += 1
                if y == '1':
                    cnt += 1
        return cnt
