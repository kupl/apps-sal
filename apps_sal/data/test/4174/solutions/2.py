n, x = map(int, input().split())

l = list(map(int, input().split()))


ans = 0

d = 0

for i in range(n):
    if d <= x:
        ans += 1
    d += l[i]

if d <= x:
    ans += 1

print(ans)
