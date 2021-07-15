n, x, y = list(map(int, input().split()))
s = input().strip()
ans = 0
for i in range(x):
    if i == y:
        ans += s[n - 1 - i] == '0'
    else:
        ans += s[n - 1 - i] == '1'
print(ans)

