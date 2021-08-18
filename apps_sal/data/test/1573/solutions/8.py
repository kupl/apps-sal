n, d = map(int, input().split())
friends = [tuple(map(int, input().split())) for i in range(n)]

friends = sorted(friends, key=lambda f: f[0])
sums = []
curr = 0
for i in range(n):
    curr += friends[i][1]
    sums.append(curr)

res = 0
for i in range(n):
    low = i
    high = n - 1
    curr = friends[i][0]
    while low < high:
        mid = (low + high + 1) // 2
        if abs(curr - friends[mid][0]) >= d:
            high = mid - 1
        else:
            low = mid
    res = max(res, sums[low] - (0 if i == 0 else sums[i - 1]))

print(res)
