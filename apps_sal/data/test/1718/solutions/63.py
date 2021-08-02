N, K = map(int, input().split())
a = list(map(int, input().split()))
if N == K:
    print(1)
else:
    tmp = N - K
    if tmp % (K - 1) == 0:
        print(1 + tmp // (K - 1))
    else:
        ans = 2 + tmp // (K - 1)
        print(ans)
