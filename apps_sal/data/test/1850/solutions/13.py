(n, k) = map(int, input().strip().split())
cr = list(map(int, input().strip().split()))
pa = list(map(int, input().strip().split()))
x = cr[k - 1] + pa[0]
p = 0
if k == 1:
    print(1)
else:
    for i in range(k - 1):
        if cr[i] + pa[-1] <= x:
            p += 1
            del pa[-1]
    print(k - p)
