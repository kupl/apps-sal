n = int(input())
a = []
m = []
e = 0
for i in range(n):
    a.append(list(map(int, input().split())))
    m.append([a[-1][0], max(a[-1][1:])])
    e = max(e, m[-1][1])
s = 0
for i in range(n):
    s += m[i][0] * (e - m[i][1])
print(s)

