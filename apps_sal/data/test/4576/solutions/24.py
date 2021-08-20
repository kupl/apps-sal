A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
for a in range(A + 1):
    if X < 500 * a:
        continue
    y = X - 500 * a
    if y == 0:
        cnt += 1
        continue
    for b in range(B + 1):
        if y < b * 100:
            continue
        z = y - 100 * b
        if z == 0:
            cnt += 1
            continue
        for c in range(C + 1):
            w = z - 50 * c
            if w == 0:
                cnt += 1
                break
print(cnt)
