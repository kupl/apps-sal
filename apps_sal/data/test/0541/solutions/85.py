N, M = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])

ans = 0
cur = -1
for i in range(M):
    a, b = ab[i]
    if a < cur:
        continue
    ans += 1
    cur = b

print(ans)
