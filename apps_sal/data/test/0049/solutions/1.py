def f(x):  # including x
    dig, cnt = 1, 9
    ans = 0
    while dig != len(str(x)):
        ans += dig * cnt
        dig += 1
        cnt *= 10
    ans += (x - (cnt // 9) + 1) * dig
    return ans


k = int(input())
l, r = 1, 1000000000000
if k == 1:
    print(1)
    return
while l < r:
    mid = (l + r + 1) >> 1
    if f(mid) < k:
        l = mid
    else:
        r = mid - 1
k -= f(l)
l += 1
print(str(l)[k - 1])
