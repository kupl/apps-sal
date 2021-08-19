(n, m) = map(int, input().split())
for _ in range(m):
    (k, *l) = map(int, input().split())
    l = set(l)
    for x in l:
        if -x in l:
            break
    else:
        print('YES')
        break
else:
    print('NO')
