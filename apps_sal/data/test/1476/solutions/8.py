l = [None, '1\n1', '1\n1', '2\n1 3', '4\n2 4 1 3']

n = int(input())
if n in range(len(l)):
    print(l[n])
else:
    print(n)
    print(' '.join(map(str, range(1, n + 1, 2))), end=' ')
    print(' '.join(map(str, range(2, n + 1, 2))))

