n = int(input())
a = [int(input()) for i in range(n)]

s = set(a)
if len(s) != 2:
    print('NO')
    return

b = list(s)
if a.count(b[0]) == a.count(b[1]):
    print('YES')
    print(b[0], b[1])
else:
    print('NO')
