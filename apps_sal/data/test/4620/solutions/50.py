n = int(input())
csf = [list(map(int, input().split())) for _ in range(n - 1)]
for i in range(n - 1):
    t = 0
    for (c, s, f) in csf[i:]:
        if s > t:
            t = s
        else:
            t += (s - t) % f
        t += c
    print(t)
print(0)
