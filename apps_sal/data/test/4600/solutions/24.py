n, m = map(int, input().split())
p, s = [], []
for _ in range(m):
    p_, s_ = input().split()
    p.append(int(p_))
    s.append(s_)

AC = [0] * n
WA = [0] * n

for i in range(m):
    if s[i] == "WA" and AC[p[i] - 1] == 0:
        WA[p[i] - 1] += 1
    elif s[i] == "AC" and AC[p[i] - 1] == 0:
        AC[p[i] - 1] += 1

for i in range(m):
    if AC[p[i] - 1] == 0:
        WA[p[i] - 1] = 0
print(sum(AC), sum(WA))
