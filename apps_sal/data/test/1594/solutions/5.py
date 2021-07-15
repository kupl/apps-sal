n, m = map(int, input().split())
d, t = [0] * (n + 1), [0] * m
for i in range(1, n + 1):
    a, b = map(int, input().split())
    d[i] = d[i - 1] + a * b
i = 1
for j, v in enumerate(map(int, input().split())):
    while v > d[i]: i += 1      
    t[j] = i
print('\n'.join(str(i) for i in t))
