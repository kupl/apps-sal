n = int(input())
names = set()
for i in range(n):
    s = input()
    if (s in names):
        print('YES')
    else:
        print('NO')
        names.add(s)
