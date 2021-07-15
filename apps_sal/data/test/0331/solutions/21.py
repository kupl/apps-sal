n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))

min_dist = n + 1
m -= 1

for i in range(len(a)):
    if a[i] > 0 and a[i] <= k:
        min_dist = min(min_dist, abs(i - m))

print(min_dist * 10)

