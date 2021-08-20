[X, N] = [int(i) for i in input().split()]
if N == 0:
    P = []
else:
    P = [int(i) for i in input().split()]
if P.count(X) == 0:
    print(X)
else:
    for i in range(100):
        if P.count(X - i) == 0:
            print(X - i)
            break
        elif P.count(X + i) == 0:
            print(X + i)
            break
