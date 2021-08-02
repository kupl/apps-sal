N = int(input())
R = []
B = []
for i in range(2 * N):
    a, b = list(map(int, input().split()))
    if i < N:
        R.append((a, b))
    else:
        B.append((a, b))
B = sorted(B)

ans = 0
checked = set()
p = []
for b in B:
    x1, y1 = b
    tR = [(x2, y2) for x2, y2 in R if x2 < x1]
    tR = sorted(tR, key=lambda p: p[1], reverse=True)
    for x2, y2 in tR:
        if (x2, y2) in checked:
            continue
        if x1 > x2 and y1 > y2:
            ans += 1
            checked.add((x2, y2))
            p.append((b, (x2, y2)))
            break
print(ans)
