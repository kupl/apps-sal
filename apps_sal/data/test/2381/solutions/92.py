(n, k) = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
res = 1
a.sort(reverse=True)
if a[0] < 0 and k % 2 == 1:
    for i in range(k):
        res = res * a[i] % mod
else:
    right = n - 1
    left = 0
    while k > 1:
        if a[right] * a[right - 1] < a[left] * a[left + 1]:
            res = res * a[left] % mod
            left += 1
            k -= 1
        else:
            res = res * a[right] * a[right - 1] % mod
            right -= 2
            k -= 2
    if k == 1:
        res = res * a[left] % mod
print(res)
