t = int(input())
for i in range(t):
    (a, b) = [int(x) for x in input().split()]
    if a < b:
        (a, b) = (b, a)
    c = a - b
    a -= 2 * c
    b -= c
    if a >= 0 and a % 3 == 0:
        print('YES')
    else:
        print('NO')
