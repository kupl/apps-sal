(n, k) = map(int, input().split())
query = sorted([tuple(map(int, input().split())) for _ in range(n)])
cnt = 0
i = 0
while cnt < k:
    (a, b) = query[i]
    cnt += b
    i += 1
print(a)
