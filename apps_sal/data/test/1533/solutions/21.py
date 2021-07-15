n = int(input())

a = []
for x in range(n):
    x = input()
    a.append(x)

lst = []
for x in a:
    if not x in lst:
        print('NO')
        lst.append(x)
    else:
        print('YES')

