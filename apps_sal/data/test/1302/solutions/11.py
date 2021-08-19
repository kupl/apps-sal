(n, k) = map(int, input().split())
if k >= n:
    print(-1)
elif k + 1 == n:
    print(' '.join(map(str, range(1, n + 1))))
else:
    print(' '.join(map(str, [k + 2] + list(range(2, k + 2)) + list(range(k + 3, n + 1)) + [1])))
