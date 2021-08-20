(N, K) = map(int, input().split())
H = sorted(map(int, input().split()))
if K == 0:
    print(sum(H))
elif N < K:
    K = N
    del H[-K:]
    print(sum(H))
else:
    del H[-K:]
    print(sum(H))
