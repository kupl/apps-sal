n = int(input())
a = list(map(int, input().split()))
r = set(a)
if len(r) <= 3:
    r = list(r)
    r.sort()
    if len(r) == 1 or len(r) == 2 or r[1] - r[0] == r[2] - r[1]:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
