n, k = list(map(int, input().split()))
a = list(map(int, input().split()))


def check(length):
    cuttings = sum((l + length - 1) // length - 1 for l in a)
    return cuttings <= k


l, r = 0, max(a)

while l + 1 < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid

print(r)
