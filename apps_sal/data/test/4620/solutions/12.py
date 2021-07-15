n = int(input())
csf = []
for i in range(n - 1):
    csf.append(list(map(int, input().split())))
for i in range(n):
    t = 0
    for j in range(n - i - 1):
        c, s, f = (csf[i + j][k] for k in range(3))
        t = (max(t - 1, s - 1) // f + 1) * f + c
    print(t)
