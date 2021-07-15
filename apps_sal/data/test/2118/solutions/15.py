n, k = list(map(int, input().split()))

lst = [i for i in range(1, n + 1)]


def rearrange(l, r):
    nonlocal k
    if k < 1 or l + 1 == r:
        return
    k -= 2
    mid = (l + r) // 2
    lst[mid - 1], lst[mid] = lst[mid], lst[mid - 1]
    rearrange(l, mid)
    rearrange(mid, r)


if k % 2 == 0 or n * 2 < k:
    print(-1)
else:
    k -= 1
    rearrange(0, n)
    print(' '.join(str(i) for i in lst))

