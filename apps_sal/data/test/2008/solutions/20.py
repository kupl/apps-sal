N = int(input())

maps = []

for i in range(N):
    a, b = list(map(int, input().split()))
    diff = b - a
    maps += [[diff, a, b]]

maps.sort()

ans = 0

for i, v in enumerate(maps):
    a = v[1]
    b = v[2]
    j = i + 1

    ans += a * (j - 1) + b * (N - j)
print(ans)
