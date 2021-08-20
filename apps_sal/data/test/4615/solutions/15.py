(a, b, c, d, e, f) = map(int, input().split())
midp = [-1 for i in range(f + 1)]
mizu = []
midp[0] = 0
for i in range(f + 1):
    if midp[i] != -1:
        if i + a * 100 <= f and midp[i + a * 100] != 0:
            midp[i + a * 100] = 0
            mizu.append(i + a * 100)
        if i + b * 100 <= f and midp[i + b * 100] != 0:
            midp[i + b * 100] = 0
            mizu.append(i + b * 100)
ans = 0
cou = [a * 100, 0]
for i in mizu:
    sai = i * e // 100
    sadp = [-1 for f in range(sai + 1)]
    sadp[0] = 0
    maxsa = 0
    for j in range(sai + 1):
        if sadp[j] != -1:
            if j + c <= sai and i + j + c <= f and (sadp[j + c] != 0):
                sadp[j + c] = 0
                maxsa = max(maxsa, j + c)
            if j + d <= sai and i + j + d <= f and (sadp[j + d] != 0):
                sadp[j + d] = 0
                maxsa = max(maxsa, j + d)
    if ans < maxsa / (i + maxsa):
        ans = maxsa / (i + maxsa)
        cou = [i + maxsa, maxsa]
print(*cou)
