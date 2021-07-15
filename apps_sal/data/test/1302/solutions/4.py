import fractions
n, k = list(map(int, input().split()))
A = [i + 1 for i in range(n)]
if k == n:
    print(-1)
else:
    good = n - 1
    i = n - 1
    while good - k > 1:
        A[i], A[i - 1] = A[i - 1], A[i]
        good -= 2
        i -= 2
    if good - k == 1:
        for i in range(1, n):
            if fractions.gcd(i + 1, A[i]) != 1:
                A[i], A[0] = A[0], A[i]
                good -= 1
                break
    if good == k:
        print(' '.join(map(str, A)))
    else:
        print(-1)

