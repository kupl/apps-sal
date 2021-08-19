(N, K) = list(map(int, input().split()))
H = sorted(list(map(int, input().split())))
if len(H) < K:
    print(0)
else:
    print(sum(H[:N - K]))
