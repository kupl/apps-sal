[N, K] = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]

if N <= K:
    print(0)
else:
    h = list(sorted(H))
    t = sum(h[0:N - K])
    print(t)
