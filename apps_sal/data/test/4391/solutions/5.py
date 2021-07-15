from itertools import accumulate

n, k = map(int, input().split())
a = map(int, input().split())
sums = [0] + list(accumulate(a))

res = 0

for l in range(k, n + 1):
    for i in range(0, n - l + 1):
        res = max(res, (sums[i + l] - sums[i]) / l)
        
print(res)
