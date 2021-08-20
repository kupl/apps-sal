(n, l) = map(int, input().split())
ans = 0
if l > 0:
    for i in range(l + 1, l + n):
        ans += i
elif n + l - 1 < 0:
    for i in range(l, l + n - 1):
        ans += i
else:
    for i in range(l, l + n):
        ans += i
print(ans)
