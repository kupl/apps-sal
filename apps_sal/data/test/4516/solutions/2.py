n, m = map(int, input().split())
a = list(map(int, input().split()))

left = [0] * (n + 1)
left_sum = left[:]
right = left[:]
cross = left[:]
rang = left[:]
ans = left[:n]
total = 0

for i in range(1, m):
    p = a[i - 1]
    q = a[i]
    if p == q:
        continue
    if q < p:
        p, q = q, p
    total += q - p
    rang[p] += 1
    rang[q - 1] -= 1
    right[p] += 1
    left[q] += 1
    left_sum[q] += q - p

start = 0
for i in range(n):
    cross[i] = start
    start += rang[i]

ans[0] = total
for i in range(2, n + 1):
    ans[i - 1] = total - cross[i] + left[i] * i - 2 * left_sum[i] + (i - 1) * right[i]
print(*ans)
