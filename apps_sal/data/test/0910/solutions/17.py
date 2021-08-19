(n, a, b) = map(int, input().split())
l = [['0'] * b for i in range(a)]
if n > a * b:
    print(-1)
else:
    for i in range(n):
        ii = i // b
        jj = i % b if ii % 2 == 0 else b - i % b - 1
        l[ii][jj] = str(i + 1)
    print('\n'.join(map(' '.join, l)))
