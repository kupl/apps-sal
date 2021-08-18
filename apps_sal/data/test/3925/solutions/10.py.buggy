import sys

s = input()

n = len(s)

if n == 1:
    print(1)
    return

for i in range(n - 1):
    if s[i] == s[i + 1] and (s[n - 1] != s[0]):
        x = s[:i + 1]
        y = s[i + 1:n]
        s = x[::-1] + y[::-1]
ans = 1
mx = 1
for i in range(1, n):
    if s[i] != s[i - 1]:
        mx += 1
    else:
        ans = max(mx, ans)
        mx = 1
print(max(mx, ans))
