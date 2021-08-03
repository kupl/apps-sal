n, m = list(map(int, input().split()))

ans = 0
rd = 10**9 + 7
if(abs(n - m) > 1):
    ans = 0
    print(ans)
elif(abs(n - m) == 1):
    tmp = min(n, m)
    tmp_mx = max(n, m)
    sm = 1
    for i in range(tmp):
        sm = (sm * (i + 1)) % rd

    ans = (sm * sm * tmp_mx) % rd
    print(ans)
else:
    sm = 1
    for i in range(n):
        sm = (sm * (i + 1)) % rd

    ans = (2 * sm * sm) % rd
    print(ans)
