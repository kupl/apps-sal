n = int(input())
if n % 2 == 0:
    print('-1')
else:
    a = list(range(n))
    print(' '.join(map(str, a)))
    print(' '.join(map(str, a)))
    print(' '.join([str((x[0] + x[1]) % n) for x in zip(a, a)]))
