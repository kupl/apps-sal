N, Z, W = map(int, input().split())
a = list(map(int, input().split()))
print(abs(W - a[0])if N == 1 else max(abs(W - a[-1]), abs(a[-1] - a[-2])))
