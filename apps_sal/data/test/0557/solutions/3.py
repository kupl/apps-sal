(n, m) = map(int, input().split())
ar = [0] * m
for x in range(n):
    (a, b) = map(int, input().split())
    ar[a:b] = [1] * (b - a)
print('YES' if set(ar) == set([1]) else 'NO')
