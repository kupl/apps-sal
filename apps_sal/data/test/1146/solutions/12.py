n, m = [int(x) for x in input().split()]
used = [False] * m
for i in range(n):
    s = [int(x) for x in input().split()]
    num = s.pop(0)
    for elem in s:
        used[elem - 1] = True
for elem in used:
    if not elem:
        print('NO')
        break
else:
    print('YES')
