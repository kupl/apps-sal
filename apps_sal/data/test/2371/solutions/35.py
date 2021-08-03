N, Z, W = map(int, input().split())
a = list(map(int, input().split()))

if N == 1:
    print(abs(W - a[N - 1]))
else:
    print(max(abs(W - a[N - 1]), abs(a[N - 1] - a[N - 2])))
