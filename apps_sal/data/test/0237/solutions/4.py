def summ(t):
    ans = (t) * (t + 1) // 2
    return ans

n, m, k = map(int, input().split())

def res(p):
    nonlocal n
    tmp = n * p
    l = k - 1
    t = min(p - 1, l)
    tmp -= summ(t)
    tmp -= (p - 1) * (l - t)
    r = n - k
    t = min(p - 1, r)
    tmp -= summ(t)
    tmp -= (p - 1) * (r - t)
    return tmp


l = 0
r = m + 1
while r - l > 1:
    mid = l + (r - l) // 2
    if res(mid) <= m:
        l = mid
    else:
        r = mid
print(l)
