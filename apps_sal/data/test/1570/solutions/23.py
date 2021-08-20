(k, n, w) = list(map(int, input().split(' ')))
tc = k * w * (w + 1) // 2
if n - tc < 0:
    print(tc - n)
else:
    print(0)
