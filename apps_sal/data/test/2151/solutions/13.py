t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    if int(a[0]) < int(''.join(a[1:n])):
        print('YES')
        print(2)
        print(a[0], ''.join(a[1:n]))
    else:
        print('NO')
