n, m = list(map(int, input().split()))
if n == 1:
    a = list(map(int, input().split()))
    print((a[0]))
else:
    A = list(map(int, input().split()))
    ans = set(A[1:])

    for _ in range(n-1):
        A = list(map(int, input().split()))
        ans = ans & set(A[1:])

    print((len(ans)))

