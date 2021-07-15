N, K = list(map(int, input().split()))

ans = 0
for i in range(2, 2*N+1):
    j = i - K
    if not 2 <= j <= 2 * N:
        continue


    ta = (i-1)-(i-1-N)*2
    A = min(i-1, ta)


    tc = (j-1)-(j-1-N)*2
    C = min(j-1, tc)




    ans += A * C

print(ans)

