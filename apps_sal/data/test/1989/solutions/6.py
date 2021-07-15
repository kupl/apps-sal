INF = 10 ** 10
# merge two sorted lists l and r
def merge(l, r):
    res = l + r
    
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res[k] = l[i]
            k += 1
            i += 1
        else:
            res[k] = r[j]
            k += 1
            j += 1

    res[k:] = l[i:] + r[j:]
    return res

def solve(fl, fr, l, r):
    if l == r:
        return 0
    
    mid = (l + r) // 2
    # after calling solve(l, mid) and (mid + 1, r), fl and fr are sorted on these ranges
    res = solve(fl, fr, l, mid) + solve(fl, fr, mid + 1, r)

    # perform 2-pointers on 2 sorted lists
    i, j = l, mid + 1
    while i <= mid:
        while j <= r and fr[j] < fl[i]:
            j += 1
        res += j - mid - 1
        i += 1
        
    # merge 2 sorted lists
    fl[l: r + 1] = merge(fl[l: mid + 1], fl[mid + 1: r + 1])
    fr[l: r + 1] = merge(fr[l: mid + 1], fr[mid + 1: r + 1])
    return res

def __starting_point():
    n = int(input())
    a = list(map(int, input().split()))

    fl, cnt = [], {}
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1
        # fl[i] = f(0, i, a[i])
        fl.append(cnt[x])

    fr, cnt = [], {}
    for x in a[::-1]:
        cnt[x] = cnt.get(x, 0) + 1
        # fr[i] = f(i, n - 1, a[i])
        fr.append(cnt[x])
    fr = fr[::-1]

    print(solve(fl, fr, 0, n - 1))

__starting_point()
