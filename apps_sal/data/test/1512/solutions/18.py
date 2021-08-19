n = int(input())
p = list(map(int, input().split()))
s = [0] * n
m1, m2 = 0, 0
for v in p:
    if m1 < v < m2:
        m1 = v
        s[m2 - 1] += 1
    elif v > m2:
        m1 = m2
        m2 = v
        s[m2 - 1] = -1
    # print(v, m1, m2, max(s))
print(s.index(max(s)) + 1)
