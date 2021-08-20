(n, m) = list(map(int, input().split()))
mn = n - min(2 * m, n)
k = 0
while k * (k - 1) // 2 < m:
    k += 1
mx = n - k
print(str(mn) + ' ' + str(mx))
