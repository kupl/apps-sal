(n, m) = list(map(int, input().split()))
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
ans = False
for y in range(n - m + 1):
    for x in range(n - m + 1):
        sol = True
        for h in range(m):
            if a[y + h][x:x + m] != b[h]:
                sol = False
                break
        if sol:
            ans = True
            break
    if ans:
        break
print('Yes' if ans else 'No')
