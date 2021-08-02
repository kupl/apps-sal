n, m = list(map(int, input().split()))

mod = 10**9 + 7
sum = 0
min = 0
max = 0

for k in range(1, n + 2):
    min += k - 1
    max += n - (k - 1)

    if k >= m:
        sum = (sum + max - min + 1) % mod
print(sum)
