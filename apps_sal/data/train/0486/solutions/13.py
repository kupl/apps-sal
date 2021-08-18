
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        n = len(S)
        for i in range(30, -1, -1):
            if N & (1 << i):
                msb = i
                break

        def get(msb):
            s = set()
            num = 0
            x = 0
            if msb > 0:
                x = 1 << (msb - 1)
            for i in range(n):
                if i == msb:
                    if S[i] == '1':
                        num += 1
                    if x < num <= N:
                        s.add(num)
                elif(i > msb):
                    if num & (1 << msb):
                        num -= (1 << msb)
                    num <<= 1
                    if S[i] == '1':
                        num += 1
                    if x < num <= N:
                        s.add(num)
                else:
                    if S[i] == '1':
                        num |= (1 << (msb - i))
            return s

        s = get(msb)
        p = 0
        if msb > 0:
            p = 1 << (msb - 1)
        if msb > 0:
            s1 = get(msb - 1)
            p = 0
            if msb > 1:
                p = 1 << (msb - 2)
            for i in s1:
                s.add(i)
        return len(s) == (N - p)
