def bbin(key, b):
    l = -1
    r = len(b)
    while r > l + 1:
        mm = (l + r) // 2
        if b[mm] >= key:
            r = mm
        else:
            l = mm
    return r


(n, m, ta, tb, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(k + 1):
    if i >= n:
        ans = -1
        break
    key = a[i] + ta
    rr = bbin(key, b) + k - i
    if rr >= m:
        ans = -1
        break
    ans = max(ans, b[rr] + tb)
print(ans)
