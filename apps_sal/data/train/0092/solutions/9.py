a = int(input())
for i in range(a):
    b = input()
    c = input()
    y = 0
    for i in b:
        if i in c:
            y = 1
        else:
            pass
    if y == 1:
        print('YES')
    else:
        print('NO')
