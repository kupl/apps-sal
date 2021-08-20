(n, k) = list(map(int, input().split()))
a = [int(i) for i in input().split()]
sum = 0
ma = 0.0
for i in range(k, n + 1):
    start = 0
    last = i
    sum = 0
    for i in range(0, last):
        sum = sum + a[i]
    ma = max(sum / (i + 1), ma)
    while last < n:
        last = last + 1
        sum = sum - a[start] + a[last - 1]
        start = start + 1
        ma = max(sum / (i + 1), ma)
print(ma)
