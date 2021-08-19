q = int(input())
for qi in range(q):
    (a, b, n, s) = list(map(int, input().split()))
    ac = s // n
    ac = min(a, ac)
    curs = ac * n
    if s - curs <= b:
        print('YES')
    else:
        print('NO')
