N, K = map(int,input().split())
if K % 2 == 1:
    c = N//K
    ans = c*(c-1)*(c-2)+3*c*(c-1)+c
    print(ans)
else:
    K //= 2
    e = 0
    o = 0
    for i in range(1, N+1):
        if i % K == 0:
            if (i//K) % 2 == 0:
                e += 1
            else:
                o += 1
    c = e
    ans = c*(c-1)*(c-2)+3*c*(c-1)+c
    c = o
    ans += c*(c-1)*(c-2)+3*c*(c-1)+c
    print(ans)
