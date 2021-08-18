n, k = list(map(int, input().split()))
k -= 1
a = list(map(int, input().split()))
tri = [1]

for x in range(2, n + 1):
    tri.append(tri[-1] + x)

if k == 0:
    print(a[0])
else:
    lo = 0
    hi = len(tri) - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if tri[mid] > k:
            hi = mid
        else:
            lo = mid

    index = k - tri[hi - 1]
    print(a[index])
