(n, k) = map(int, input().split())
a = list(map(int, input().split()))
summ = 0
multi = 1
for i in range(n):
    if n - i > k and multi < k:
        summ += a[i] * multi
        multi += 1
    elif n - i > k or i + 1 < k:
        summ += a[i] * multi
    elif n - i <= k:
        summ += a[i] * multi
        multi -= 1
print(summ / (n - k + 1))
