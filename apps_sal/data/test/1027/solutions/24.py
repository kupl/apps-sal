l = list(map(int, input().split()))
ms = 0
for i in range(14):
    if l[i] > 0:
        d = l[i] // 14
        o = l[i] % 14
        nl = [l[k] for k in range(len(l))]
        nl[i] = 0
        for j in range(len(l)):
            nl[j] += d
        j = i + 1
        j %= 14
        for vbn in range(o):
            nl[j] += 1
            j += 1
            j %= 14
        s = 0
        for m in range(len(l)):
            if nl[m] % 2 == 0:
                s += nl[m]
        ms = max(ms, s)
print(ms)
