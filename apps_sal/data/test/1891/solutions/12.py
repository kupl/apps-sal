(n, k, A, B) = list(map(int, input().split()))


def solve(l, r, a):
    if len(a) == 0:
        return A
    if l == r:
        return B * len(a)
    mid = (l + r) // 2
    lx = []
    rx = []
    for i in a:
        if i <= mid:
            lx.append(i)
        else:
            rx.append(i)
    return min(B * len(a) * (r - l + 1), solve(l, mid, lx) + solve(mid + 1, r, rx))


a = list(map(int, input().split()))
print(solve(1, 1 << n, a))
