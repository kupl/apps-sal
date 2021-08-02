n = int(input())
for _ in range(n):
    a = input()
    b = input()
    a = a[::-1]
    b = b[::-1]
    indb = 0
    for i in range(len(b)):
        if b[i] == '1':
            indb = i
            break
    inda = 0
    for i in range(indb, len(a)):
        if a[i] == '1':
            inda = i
            break

    print(max(inda - indb, 0))
