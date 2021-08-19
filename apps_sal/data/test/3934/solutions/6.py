n = int(input())
degrees = [0 for _ in range(n)]
for _ in range(n - 1):
    (u, v) = tuple(map(int, input().rstrip().split()))
    degrees[u - 1] += 1
    degrees[v - 1] += 1
res = 'YES'
for d in degrees:
    if d == 2:
        res = 'NO'
print(res)
