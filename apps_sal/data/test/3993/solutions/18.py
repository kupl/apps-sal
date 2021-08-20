(n, m, k) = list(map(int, input().split()))
ps = list(map(int, input().split()))
shift = 0
res = 0
ind = 0
while len(ps) > ind:
    res += 1
    first = (ps[ind] - shift - 1) // k * k + 1
    ds = 0
    while len(ps) > ind and ps[ind] - shift - first < k:
        ds += 1
        ind += 1
    shift += ds
print(res)
