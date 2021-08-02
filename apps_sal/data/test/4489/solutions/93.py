n = int(input())
S = []
T = []
data = set()
for i in range(n):
    s = input()
    S.append(s)
    data.add(s)
m = int(input())
for i in range(m):
    t = input()
    T.append(t)
    data.add(t)
ans = 0
for i in data:
    ans = max(ans, S.count(i) - T.count(i))
print(ans)
