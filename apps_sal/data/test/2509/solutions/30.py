n, k = map(int, input().split())

sum = 0
for b in range(k + 1, n + 1):
    re = n // b
    sum += re * (b - k)
    if k <= n % b:
        sum += n % b - k + 1
if k == 0:
    sum -= n
print(sum)
