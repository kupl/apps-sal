n = int(input())
s = [input().split() for i in range(n)]
m = int(input())
t = [input().split() for i in range(m)]
ans = 0
for i in range(n):
    temp = s.count(s[i]) - t.count(s[i])
    ans = max(ans, temp)
print(ans)
