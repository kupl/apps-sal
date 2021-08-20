(a, b) = map(int, input().split())
R = [b]
ok = 1
while b > a:
    while b % 10 != 1 and b > a:
        if b % 2 == 1:
            ok = 0
            break
        else:
            b = b // 2
            R += [b]
    if b > a:
        b = (b - 1) // 10
        R += [b]
if ok == 0 or b < a:
    print('NO')
else:
    print('YES')
    print(len(R))
    for i in range(len(R)):
        print(R[len(R) - 1 - i], end=' ')
