(a, b, c) = map(int, input().split())
d = []
for i in range(1, b + 1):
    d.append(a * i % b)
if c in d:
    print('YES')
else:
    print('NO')
