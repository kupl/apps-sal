n = int(input())
(a, b) = (1, 2)
c = 3
m = []
for i in range(n):
    m.append(int(input()))
for x in m:
    if x == a:
        (b, c) = (c, b)
    elif x == b:
        (a, c) = (c, a)
    else:
        print('NO')
        break
else:
    print('YES')
