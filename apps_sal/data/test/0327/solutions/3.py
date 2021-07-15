N, K = list(map(int, input().split()))

if K == 1:
    print(N)
else:
    cnt = 0
    while N > 0:
        N >>= 1
        cnt += 1
    print((1<<cnt)-1)

