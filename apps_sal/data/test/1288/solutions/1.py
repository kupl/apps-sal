def subsolve(a, x):
    c = 0
    i = 0
    while i < len(a):
        if a[i] > x:
            i += 1
            continue
        j = i
        while j < len(a) and a[j] <= x:
            j += 1
        c += (j - i) // 2 + (j - i) % 2
        i = j
    return c

def odd(n, k, a):
    if k >= 2 and k % 2 == 0:
        a = a[:-1]
    l, r = 0, max(a) + 1
    while r - l > 1:
        mid = (l + r) // 2
        if subsolve(a, mid) >= k // 2 + k % 2:
            r = mid
        else:
            l = mid
    return r

def even(n, k, a):
    if k == 1:
        return max(a) + 1
    a = a[1:]
    if k % 2 == 1:
        a.pop(-1)
    l, r = 0, max(a) + 1
    while r - l > 1:
        mid = (l + r) // 2
        if subsolve(a, mid) >= k // 2:
            r = mid
        else:
            l = mid
    return r

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(min(odd(n, k, a), even(n, k, a)))

solve()
