from fractions import gcd
(n, a, v) = (int(input()), list(map(int, input().split())), [])
for (i, ai) in enumerate(a):
    v.append(ai)
    if i < n - 1 and gcd(ai, a[i + 1]) > 1:
        v.append(1)
print(len(v) - len(a))
print(' '.join(map(str, v)))
