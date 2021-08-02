N = int(input())
K = int(input())
xs = list(map(int, input().split()))

dist_sum = 0
for i in range(N):
    y = i + 1
    x = xs[i]

    if x > K - x:
        dist_sum += (K - x) * 2
    else:
        dist_sum += x * 2

print(dist_sum)
