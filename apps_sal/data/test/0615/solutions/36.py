from itertools import accumulate as ac
n = int(input())
s = list(ac(list(map(int, input().split()))))
c = 0
d = 2
f = s[-1]
k = f
for i in range(1, n - 1):
    while s[i] > s[c] + s[c + 1]:
        c += 1
    while s[i] + f > s[d] + s[d + 1]:
        d += 1
    j = [s[c], s[i] - s[c], s[d] - s[i], f - s[d]]
    k = min(max(j) - min(j), k)
print(k)
