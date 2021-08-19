q = int(input())
for rwere in range(q):
    a = input()
    b = input()
    c = input()
    n = len(a)
    dasie = True
    for i in range(n):
        if c[i] == a[i] or c[i] == b[i]:
            continue
        else:
            dasie = False
    if dasie:
        print('YES')
    else:
        print('NO')
