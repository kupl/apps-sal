n = int(input())
a = list(map(int, input().split()))
b = []
for i, aa in enumerate(a):
    b.append(aa - (i + 1))
b.sort()
s1, s2 = 0, 0
m1, m2 = 0, 0
if n % 2 == 0:
    m1 = b[n // 2]
    m2 = b[n // 2 + 1]
    for bb in b:
        s1 += abs(bb - m1)
        s2 += abs(bb - m2)
    print((min(s1, s2)))
else:
    m1 = b[n // 2]
    for bb in b:
        s1 += abs(bb - m1)
    print(s1)
