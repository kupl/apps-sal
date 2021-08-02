q = int(input())
a = list(map(int, input().split()))
ans = 0
t = q
for i in range(q - 1, -1, -1):
    if t > i:
        ans += 1
    t = min(t, i - a[i])
print(ans)
