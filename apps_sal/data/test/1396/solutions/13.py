from itertools import *
def R(): return map(int, input().split())


n, k, x = R()
c = [(k, len(list(g))) for k, g in groupby(R())]
count = 0
for i in range(len(c)):
    if c[i][0] == x and c[i][1] > 1:
        a = c[i][1]
        l, r = i - 1, i + 1
        while l >= 0 and r < len(c) and c[l][0] == c[r][0] and c[l][1] + c[r][1] > 2:
            a += c[l][1] + c[r][1]
            l -= 1
            r += 1
        count = max(count, a)
print(count)
