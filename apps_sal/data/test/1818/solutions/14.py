def C(x):
    s = bin(x)[2:]
    c = 0
    for t in s:
        if t == '1':
            c += 1
    return c


n = input();

ar = list(map(int, input().split()))
bu = {}

for e in ar:
    c = C(e)
    if c not in bu:
        bu[c] = 0
    bu[c] += 1

S = 0
for v in list(bu.values()):
    S += v * (v - 1) // 2

print(S)
