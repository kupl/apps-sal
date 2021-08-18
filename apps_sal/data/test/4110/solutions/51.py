d, g = map(int, input().split())
g //= 100
A = []
for i in range(d):
    p, c = map(int, input().split())
    c //= 100
    A.append([i + 1, p, c])
ans = float("inf")
for bit in range(1 << d):
    now = 0
    mon = 0
    for i in range(d):
        if bit >> i & 1:
            now += A[i][0] * A[i][1] + A[i][2]
            mon += A[i][1]
    if now >= g:
        ans = min(ans, mon)
        continue

    for i in range(d - 1, -1, -1):
        if bit >> i & 1 == 0:
            for j in range(A[i][1]):
                now += A[i][0]
                mon += 1
                if now >= g:
                    ans = min(ans, mon)
                    continue
                else:
                    continue
print(ans)
