getints = lambda: map(int, input().split())
n, a, b = getints()
ans = 0
for i in range(1, n+1):
    s = str(i)
    sum = 0
    for c in s:
        sum += int(c)
    if a <= sum <= b:
        ans += i
print(ans)
