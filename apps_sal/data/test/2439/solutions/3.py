T = int(input())

for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]

    s = sum(A)
    if s == 0:
        print('NO')
    else:
        print('YES')
        if s > 0:
            B = sorted(A, reverse=True)
        else:
            B = sorted(A)
        print(' '.join(map(str, B)))

