def my(a, b, c):
    for x, y in zip(a, b):
        for z in range(4):
            if c[-1] | z == x and c[-1] & z == y:
                c += [z]
                break
        else:
            return []
    return c


n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

for i in range(4):
    t = my(a, b, [i])
    if t:
        print('YES')
        print(*t)
        break
else:
    print('NO')
