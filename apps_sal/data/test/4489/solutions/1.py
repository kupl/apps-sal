n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ans = 0
cnt = 0
for i in set(s):
    cnt = s.count(i) - t.count(i)
    ans = max(ans, cnt)
print(ans)
