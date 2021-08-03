k = int(input())
if k > 36:
    print(-1)
else:
    v = k // 2
    n = k % 2
    print(v * '8' + n * '6')
