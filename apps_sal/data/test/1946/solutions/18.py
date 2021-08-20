n = int(input().strip())
a = [tuple(map(int, input().strip().split())) for _ in range(n)]
m = int(input().strip())
a.extend((tuple(map(int, input().strip().split())) for _ in range(m)))
a.sort()
a.append((0, 0))
res = 0
i = 0
while i < n + m:
    if a[i][0] == a[i + 1][0]:
        res += max(a[i][1], a[i + 1][1])
        i += 2
    else:
        res += a[i][1]
        i += 1
print(res)
