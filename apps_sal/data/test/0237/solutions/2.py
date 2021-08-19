def f(med):
    left = k - 1
    right = n - k
    #print(med, left, right)
    ans = 0
    if med > left + 1:
        d = med - left
        ans += (med + d) * (med - d + 1) // 2
    else:
        ans += med * (med + 1) // 2
        left -= (med - 1)
        ans += left
    # print(ans)
    if med > right + 1:
        d = med - right
        ans += (med + d) * (med - d + 1) // 2
    else:
        ans += med * (med + 1) // 2
        right -= (med - 1)
        ans += right
    # print(ans)
    if ans - med <= m:
        return True
    else:
        return False


n, m, k = list(map(int, input().split()))
l = 1
r = m + 1
while r - l > 1:
    med = (r + l) // 2
    if f(med):
        l = med
    else:
        r = med
print(l)
