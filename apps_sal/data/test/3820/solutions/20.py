(n, m) = (int(x) for x in input().split())
a = input()
b = input()
if '*' not in a:
    if a == b:
        print('YES')
    else:
        print('NO')
    quit()
(l, r) = a.split('*')
if len(b) >= len(a) - 1:
    if l == b[:len(l)] and r == b[len(b) - len(r):]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
