def go():
    (n, k) = (int(i) for i in input().split(' '))
    s = [int(i) for i in input().split(' ')]
    c = 0
    so_far = set()
    o = []
    for i in range(n):
        if c == k:
            break
        if s[i] not in so_far:
            so_far.add(s[i])
            o.append(i)
            c += 1
    if c == k:
        print('YES')
        print(' '.join((str(i + 1) for i in o)).strip())
    else:
        print('NO')


go()
