(X, N) = map(int, input().split())
if N != 0:
    p = set(map(int, input().split()))
    for i in range(N):
        if X - i not in p:
            print(X - i)
            break
        elif X + i not in p:
            print(X + i)
            break
    else:
        print(X - i - 1)
else:
    print(X)
