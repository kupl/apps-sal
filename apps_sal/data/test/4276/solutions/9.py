(n, T) = map(int, input().split())
a = 1001
for _ in range(n):
    (c, t) = map(int, input().split())
    if t <= T and c < a:
        a = c
if a == 1001:
    print('TLE')
else:
    print(a)
