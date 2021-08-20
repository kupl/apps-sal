(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
count = 0
curr = 0
i = n
while count < m and i >= 0:
    i -= 1
    if curr + a[i] <= k:
        curr += a[i]
    else:
        count += 1
        curr = a[i]
print(n - i - 1)
