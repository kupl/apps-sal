n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        print('YES')
    else:
        print('NO')
        d[s] = 1
