n, k = map(int, input().split())
ab = sorted([list(map(int, input().split())) for _ in range(n)])
cnt = 0
for a, b in ab:
    cnt += b
    if cnt >= k:
        break
print(a)
