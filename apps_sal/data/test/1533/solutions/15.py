n = int(input())
lst = []
for i in range(n):
    s = input()
    if s in lst:
        print('YES')
    else:
        lst.append(s)
        print('NO')
