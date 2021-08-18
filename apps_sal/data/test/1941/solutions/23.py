a, b, n = list(map(int, input().split()))
lis = [0] + [(a + i * b) for i in range(1000001)]
for i in range(n):
    ll, t, m = list(map(int, input().split()))
    l = ll
    r = (t - a) // b + 1
    while l <= r:
        mid = l + (r - l) // 2
        ter = mid - ll + 1
        su = ((ter) * (2 * lis[ll] + (ter - 1) * b)) // 2
        if t * m >= su and lis[mid] <= t:
            l = mid + 1
        else:
            r = mid - 1
    if l == ll:
        print(-1)
    else:
        print(r)
