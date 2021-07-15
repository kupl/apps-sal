N, *X = list(map(int, open(0).read().split()))
sorted_X = sorted(X)
median_l = sorted_X[N // 2 - 1]
median_r = sorted_X[N // 2]

for x in X:
    if x < median_l:
        print(median_r)
    elif x == median_l:
        print(median_r)
    elif x == median_r:
        print(median_l)
    else:
        print(median_l)

