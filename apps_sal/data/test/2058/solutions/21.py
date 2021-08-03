p = input()
s = input()
n = len(s)
ans = 0
dl = len(s) - len(p)
m = ([(0, 0), (0, 1)] if s[0] == '1' else [(0, 0), (1, 0)])
for i in range(1, n):
    if s[i] == '0':
        m.append((m[-1][0] + 1, m[-1][1]))
    else:
        m.append((m[-1][0], m[-1][1] + 1))

for i in range(len(p)):
    if p[i] == '0':
        ans += (m[dl + i + 1][1] - m[i][1])
    else:
        ans += (m[dl + i + 1][0] - m[i][0])
print(ans)
