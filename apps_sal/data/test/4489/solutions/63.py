n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

ans = 0
for i in set(s):
    ans = max(s.count(i) - t.count(i), ans)
print(ans)
