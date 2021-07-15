n = int(input())
s = [input().split() for _ in range(n)]
m = int(input())
t = [input().split() for _ in range(m)]
ans = -100
for i in s:
    ans = max(ans,s.count(i) - t.count(i))
if ans < 0:
    ans = 0
print(ans)
