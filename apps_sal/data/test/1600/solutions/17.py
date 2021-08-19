(n, s, v) = (int(input()), 0, 0)
a = list(map(int, input().split()))
for (ai, bi) in zip(a, sorted(a)):
    s += bi - ai
    v += not s
print(v)
