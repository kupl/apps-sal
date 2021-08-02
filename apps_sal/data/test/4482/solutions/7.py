N = int(input())
*A, = list(map(int, input().split()))

mx = max(A)
mn = min(A)


if len(set(A)) == 1:
    print((0))
else:
    ans = float('inf')
    for i in range(mn, mx):
        ans = min(ans, sum([(k - i)**2 for k in A]))
    print(ans)
