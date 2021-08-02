n, k = list(map(int, input().split()))
H = sorted(list(map(int, input().split())))
if n <= k:
    print((0))
    return
if k == 0:
    print((sum(H)))
    return
print((sum(H[:-k])))
