n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a = a[::-1]

res = 0
weight = 0

for i in range(n):
    weight += a[i]
    if weight > k:
        weight = a[i]
        m -= 1
    if m <= 0:
        break
    res += 1

print(res)
