input()
s0 = input()
s1 = input()
if s0.count('1') != s1.count('1'):
    print(-1)
else:
    m0 = 0
    m1 = 0
    v0 = 0
    v1 = 0
    for i, j in zip(s0, s1):
        if i != j:
            v0 += 1 if i == '1' else -1
            v1 += 1 if j == '1' else -1
            m0 = max(v0, m0)
            m1 = max(v1, m1)
    print(m0 + m1)
