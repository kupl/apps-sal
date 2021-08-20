def d_NoNeed(N, K, A):
    a = sorted(A)
    s = t = 0
    for i in range(N - 1, -1, -1):
        if s + a[i] < K:
            s += a[i]
            t += 1
        else:
            t = 0
    return t


(N, K) = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print(d_NoNeed(N, K, A))
