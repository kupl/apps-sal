n = int(input())
csf = []
for i in range(n - 1):
    c, s, f = list(map(int, input().split()))
    csf.append([c, s, f])

for i in range(n):
    t = 0
    for j in range(i, n - 1):
        c, s, f = csf[j]
        if t <= s:
            t = s + c
        else:
            if t % f == 0:
                w = 0
            else:
                w = f - t % f
            t = t + w + c
    print(t)
