N, K = map(int, input().split())
ans = N
a = ans // K
b = ans % K

if a > 0:
    ans = N - K * a
    a = ans // K
    b = ans % K

if a == 0:
    if ans > abs(ans - K):
        print(abs(ans - K))
    else:
        print(ans)
