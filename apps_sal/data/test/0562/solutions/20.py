def lol(a):
    c = 0
    for x in a:
        if x[1] == 1:
            c += 1
        else:
            c -= 1
        if c >= 3:
            return 0
    return 1


n = int(input())
a = []
for _ in range(n):
    (x, y) = map(int, input().split())
    a.append([x, 1])
    a.append([y, 2])
a = sorted(a)
print('YES' if lol(a) else 'NO')
