n, m = list(map(int, input().split()))
condition = [list(map(int, input().split())) for _ in range(m)]

condition.sort(key=lambda a: (a[1], a[0]))

right_end = 0
ans = 0
for c in condition:
    if c[0] >= right_end:
        ans += 1
        right_end = c[1]
print(ans)
