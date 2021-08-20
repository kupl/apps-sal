(n, m) = map(int, input().split())
dd = set()
a = b = c = 0
for i in range(n):
    s = input()
    dd.add(s)
    a += 1
for i in range(m):
    s = input()
    if s in dd:
        a -= 1
        b += 1
    else:
        c += 1
b %= 2
a += b
if a > c:
    print('YES')
else:
    print('NO')
