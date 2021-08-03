s = list(str(input()))
n = len(s)
ans = 10**10
for i in range(n - 1):
    if s[i] != s[i + 1]:
        ans = min(ans, max(i + 1, n - i - 1))

if ans == 10**10:
    print(n)
else:
    print(ans)
