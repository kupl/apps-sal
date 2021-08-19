(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ptr = 0
while a[ptr] == 0:
    ptr += 1


def check(x):
    if x == 0:
        return max(a) >= k
    binomial = 1
    sum = 0
    for i in range(n - ptr):
        if binomial >= k:
            return True
        sum += binomial * a[n - i - 1]
        binomial *= x + i
        binomial //= i + 1
        if sum >= k:
            return True
    return False


(lo, hi) = (0, k)
while lo < hi:
    md = (lo + hi) // 2
    if check(md):
        hi = md
    else:
        lo = md + 1
print(lo)
