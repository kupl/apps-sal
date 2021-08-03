n, k = list(map(int, input().split()))
xs = list(map(int, input().split()))
start = xs[0]
result = 1

for i, x in enumerate(xs):
    if (x - start) <= k:
        continue
    if i == 0 or xs[i] - xs[i - 1] > k:
        print(-1)
        break
    result += 1
    start = xs[i - 1]
else:
    print(result)
