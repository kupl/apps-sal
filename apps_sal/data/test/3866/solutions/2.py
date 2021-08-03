n = int(input())
if n & 1:
    t = ' '.join(map(str, range(n)))
    print(t)
    print(t[2:] + ' 0')
    print(' '.join(map(str, list(range(1, n, 2)) + list(range(0, n, 2)))))
else:
    print(-1)
