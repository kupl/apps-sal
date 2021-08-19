(n, m) = list(map(int, input().split()))
h = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]
good = [True] * n
for i in range(m):
    if h[ab[i][0] - 1] < h[ab[i][1] - 1]:
        good[ab[i][0] - 1] = False
    elif h[ab[i][0] - 1] > h[ab[i][1] - 1]:
        good[ab[i][1] - 1] = False
    else:
        good[ab[i][0] - 1] = False
        good[ab[i][1] - 1] = False
print(good.count(True))
