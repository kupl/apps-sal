n, k = list(map(int, input().split()))
x = [int(i) for i in input().split()]
count = 1
i = 0
f = False
while (x[i] + k < x[-1]):
    if x[i] + k in x:
        i = x.index(x[i] + k)
    else:
        f = False
        max = 0
        for j in range(i, n):
            if x[j] - x[i] <= k:
                max = j
            else:
                break
        if max == i:
            f = True
            break
        else:
            i = max
    count += 1
if f:
    print(-1)
else:
    print(count)
