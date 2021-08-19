N = int(input())
A = list(map(int, input().split()))
rate = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
ratez = {'z': 0}
for i in range(N):
    if A[i] >= 1 and A[i] <= 399:
        rate['a'] += 1
    if A[i] >= 400 and A[i] <= 799:
        rate['b'] += 1
    if A[i] >= 800 and A[i] <= 1199:
        rate['c'] += 1
    if A[i] >= 1200 and A[i] <= 1599:
        rate['d'] += 1
    if A[i] >= 1600 and A[i] <= 1999:
        rate['e'] += 1
    if A[i] >= 2000 and A[i] <= 2399:
        rate['f'] += 1
    if A[i] >= 2400 and A[i] <= 2799:
        rate['g'] += 1
    if A[i] >= 2800 and A[i] <= 3199:
        rate['h'] += 1
    if A[i] >= 3200:
        ratez['z'] += 1
keys = [k for (k, v) in rate.items() if v != 0]
if ratez['z'] == 0:
    print(len(keys), len(keys))
elif len(keys) == 0:
    print(1, ratez['z'])
else:
    print(len(keys), len(keys) + ratez['z'])
