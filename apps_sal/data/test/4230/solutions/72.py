(X, N) = list(map(int, input().split()))
p = list(map(int, input().split()))
k = 0
if N != 0:
    while X - k in p and X + k in p:
        k += 1
    if X - k not in p:
        print(X - k)
    else:
        print(X + k)
else:
    print(X)
