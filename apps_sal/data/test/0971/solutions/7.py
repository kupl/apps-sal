n, b, d = list(map(int, input().split()))

cur = 0
ans = 0
for a in list(map(int, input().split())):
    if a > b:
        continue

    cur += a
    if cur > d:
        cur = 0
        ans += 1

print(ans)
