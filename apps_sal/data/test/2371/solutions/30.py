N, Z, W = map(int, input().split())
a = list(map(int, input().split()))
if N == 1:
    print(abs(W - a[0]))
else:
    print(max(abs(a[-1] - a[-2]), abs(W - a[-1])))
