n = int(input())
for i in range(n):
    a = input()
    b = input()
    a, b = min(a, b), max(a, b)
    h = True
    for j in range(len(a)):
        if a[j] in b:
            print('YES')
            h = False
            break
    if h:
        print('NO')
