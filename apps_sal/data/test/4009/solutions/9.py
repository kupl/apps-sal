(n, x, y) = list(map(int, input().split()))
s = input()
ans = 0
for i in range(n - x, n):
    if i == n - y - 1:
        if s[i] == '0':
            ans += 1
    elif s[i] == '1':
        ans += 1
print(ans)
