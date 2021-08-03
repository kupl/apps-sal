def f(a):
    sums1 = 0
    sums2 = 0
    if k >= a:
        sums1 = a * (a + 1) // 2
        sums1 += k - a
    else:
        sums1 = k * (a + a - k + 1) // 2

    sums3 = 0
    sums4 = 0
    k1 = n - k + 1
    if k1 >= a:
        sums2 = a * (a + 1) // 2
        sums2 += k1 - a
    else:
        sums2 = k1 * (a + a - k1 + 1) // 2
    if sums1 + sums2 - a <= m:
        return True
    else:
        return False


n, m, k = map(int, input().split())
left = 1
right = 10**9 + 5

while left + 1 != right:
    mid = (left + right) // 2
    if f(mid):
        left = mid
    else:
        right = mid
if f(right):
    print(right)
else:
    print(left)
