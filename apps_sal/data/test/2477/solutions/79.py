n, k = map(int, input().split())
A = tuple(map(int, input().split()))
A = sorted(A, reverse=True)

l = 0
r = max(A) + 1


def cut(l, k):
    for a in A:
        if a > l:
            k -= (-(-a // l) - 1)
    return k >= 0


while r - l > 1:
    mid = (r + l) // 2
    if cut(mid, k):
        r = mid
    else:
        l = mid
print(r)
