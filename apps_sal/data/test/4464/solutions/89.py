a, b, c = map(int, input().split())
d = a % b
s = set()
while d not in s:
    s.add(d)
    d = (d + a) % b
if c in s:
    print('YES')
else:
    print('NO')
