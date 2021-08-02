n = int(input())
s, t = map(str, input().split())
ans = []
for i in range(len(s)):
    ans.append(s[i])
    ans.append(t[i])
ans = "".join(ans)
print(ans)
