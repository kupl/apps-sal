s = list(input())
n = len(s)
ans = 0

for i in range(n // 2):
    if s[i] != s[-1 - i]:
        ans += 1

print(ans)
