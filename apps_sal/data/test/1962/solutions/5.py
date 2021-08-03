n, k, l = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
if L[n - 1] - L[0] > l:
    print(0)
else:
    F = L[0:n]
    D = []
    # print(F)
    count = 0
    ss = 0
    for i in range(n, n * k):
        if L[i] - L[0] <= l:
            F.append(L[i])
            count += 1
            if count == k - 1:
                D.append(L[ss])
                ss += k
                count = 0
        else:
            break
    # print(F[ss:])
    # print(D)
    if count == 0:
        print(sum(F[ss:]) + sum(D))
    else:
        print(F[ss] + sum(F[ss + count + 1:]) + sum(D))
