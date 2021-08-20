n = int(input()) + 1
res = 0
a = tuple(map(int, input().split()))
for ai in a:
    res += ai * (n - ai)
for (ai, aj) in map(sorted, list(zip(a, a[1:]))):
    res -= ai * (n - aj)
print(res)
