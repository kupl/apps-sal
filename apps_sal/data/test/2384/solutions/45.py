n = int(input())
a = list(map(int, input().split()))
m0 = 0
m1 = 0
m2 = 0
if n % 2 == 0:
    for (i, ai) in enumerate(a):
        if i % 2 == 0:
            m0 += ai
        else:
            m1 = max(m0, m1 + ai)
    print(max(m0, m1))
else:
    for (i, ai) in enumerate(a):
        if i % 2 == 0:
            if i > 0:
                m2 = max(m2 + ai, m1, m0)
            if i < n - 1:
                m0 += ai
        else:
            m1 = max(m0, m1 + ai)
    print(max(m0, m1, m2))
