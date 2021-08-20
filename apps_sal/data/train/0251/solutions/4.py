class Solution:

    def clumsy(self, N: int) -> int:
        flag = 1
        temp = 0
        cur = 0
        i = 1
        for j in range(N, 0, -1):
            if i % 4 == 1:
                cur = flag * j
            elif i % 4 == 2:
                cur *= j
            elif i % 4 == 3:
                cur = int(cur / j)
            else:
                cur += j
                temp += cur
                flag = -1
                cur = 0
            i += 1
        return temp + cur
