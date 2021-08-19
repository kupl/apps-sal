(N, Z, W) = (int(x) for x in input().split())
a = list(map(int, input().split()))
if N == 1:
    print(abs(W - a[0]))
else:
    print(max(abs(a[-1] - W), abs(a[-1] - a[-2])))
