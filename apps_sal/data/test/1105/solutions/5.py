p = {}
for i in range(int(input())):
    x, k = map(int, input().split())
    if k in p:
        if x == p[k] + 1: p[k] = x
        elif x > p[k]:
            print('NO')
            return
    elif x:
        print('NO')
        return
    else:
        p[k] = 0
print('YES')
