(h, w, k) = list(map(int, input().split()))
choco = [[0] * w for _ in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        choco[i][j] = int(s[j])
ans = float('inf')
for bit in range(1 << h - 1):
    idx = [0] * h
    group = 0
    for i in range(h):
        idx[i] = group
        if bit >> i & 1:
            group += 1
    group += 1
    array = [[0] * w for _ in range(group)]
    for j in range(w):
        for i in range(h):
            array[idx[i]][j] += choco[i][j]
    cnt = group - 1
    cum = [0] * group
    canAdd = True
    for i in range(w):
        for j in range(group):
            if cum[j] > k:
                canAdd = False
        if ans <= cnt:
            canAdd = False
        if canAdd is False:
            break
        for j in range(group):
            tmp = cum[j] + array[j][i]
            if tmp > k:
                cnt += 1
                for l in range(group):
                    cum[l] = array[l][i]
                break
            cum[j] += array[j][i]
    if canAdd:
        ans = min(ans, cnt)
print(ans)
