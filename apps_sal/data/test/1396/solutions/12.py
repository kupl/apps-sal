(n, k, x) = list(map(int, input().split()))
L = list(map(int, input().split()))
ans = 0
for i in range(n):
    X = list(L[0:i]) + [x] + list(L[i:])
    a = 0
    while 1:
        cont = False
        cnt = 1
        z = 0
        for i in range(1, len(X)):
            if X[i] == X[i - 1]:
                cnt += 1
            elif cnt >= 3:
                X = list(X[0:z]) + list(X[i:])
                cont = True
                break
            else:
                cnt = 1
                z = i
        if cont:
            continue
        if cnt >= 3:
            X = list(X[:z])
            continue
        break
    ans = max(ans, n - len(X))
print(ans)
