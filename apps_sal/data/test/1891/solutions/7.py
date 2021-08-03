from bisect import bisect_left as lb, bisect_right as ub

n, k, A, B = map(int, input().split(' '))
a = sorted(map(int, input().split(' ')))


def heihei(l, r):
    cnt = ub(a, r) - lb(a, l)
    if cnt == 0:
        return A

    if l == r:
        return A if cnt == 0 else B * cnt

    mid = (l + r) >> 1
    lr, rr = heihei(l, mid), heihei(mid + 1, r)

    return min(B * cnt * (r - l + 1), lr + rr)


print(heihei(1, 2 ** n))
