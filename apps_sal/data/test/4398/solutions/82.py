n = int(input())
s, t = map(str, input().split())
ans = []
for i in range(n):
    ans.append(s[i] + t[i])
ans = "".join(ans)
print(ans)
