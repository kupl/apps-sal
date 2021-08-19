n = int(input())
(s, t) = map(str, input().split())
ans = ''
for i in range(n):
    ans = ans + s[i]
    ans = ans + t[i]
print(ans)
