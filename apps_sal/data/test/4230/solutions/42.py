X, N = map(int, input().split())
p = list(map(int, input().split()))

if N ==0 or X < min(p) or X > max(p):
    print(X)
else:
    for n in range(N+1):
        if not X - n in p:
            print(X - n)
            break
        elif not X + n in p:
            print(X + n)
            break
