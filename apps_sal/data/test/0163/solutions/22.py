n, k = list(map(int, input().split()))
s = input()
a = s.index('G')
b = s.index('T')
d = [0] * 1000
d[a] = 1
for j in range(200):
    for i in range(n):
        if i - k >= 0 and d[i - k] == 1 and s[i] != '#':
            d[i] = 1
        if d[i + k] == 1 and s[i] != '#':
            d[i] = 1
if d[b]:
    print('YES')
else:
    print('NO')

