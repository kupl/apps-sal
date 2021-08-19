(n, k) = list(map(int, input().split()))
m = input()
d = {chr(ord('A') + i): 0 for i in range(26)}
for ch in m:
    d[ch] += 1
nw = [[ch, d[ch]] for ch in d]
fl = True
while fl:
    fl = False
    for i in range(25):
        if nw[i][1] < nw[i + 1][1]:
            d = nw[i][:]
            nw[i] = nw[i + 1][:]
            nw[i + 1] = d[:]
            fl = True
s = 0
i = 0
while k > 0:
    if k >= nw[i][1]:
        s += nw[i][1] ** 2
        k -= nw[i][1]
    else:
        s += k ** 2
        k = 0
    i += 1
print(s)
