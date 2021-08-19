n = int(input())
(s, t) = list(input().split())
ans = ''
for i in range(n):
    ans += s[i] + t[i]
print(ans)
