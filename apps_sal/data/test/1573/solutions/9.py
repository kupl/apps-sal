(n, d) = map(int, input().split())
a = [tuple(map(int, input().split())) for i in range(n)]
a.sort(reverse=True)
sums = [0] * n
sums[0] = a[0][1]
for i in range(1, n):
    sums[i] = sums[i - 1] + a[i][1]
maxsum = 0
r = 0
for l in range(n):
    if r < l:
        r = l
    while r < n and -a[r][0] + a[l][0] < d:
        r += 1
    r -= 1
    if l > 0:
        summ = sums[r] - sums[l - 1]
    else:
        summ = sums[r]
    maxsum = max(maxsum, summ)
print(maxsum)
