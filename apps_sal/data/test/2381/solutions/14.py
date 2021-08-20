def solve(n, k, a):
    mod = 10 ** 9 + 7
    ans = 1
    l = 0
    r = n - 1
    a.sort()
    if k % 2 == 1:
        ans *= a[r]
        r -= 1
    if ans < 0:
        ans = 1
        for i in range(k):
            ans *= a[n - i - 1]
            ans %= mod
        return ans
    for i in range(k // 2):
        tmp_min = a[l] * a[l + 1]
        tmp_max = a[r] * a[r - 1]
        if tmp_max > tmp_min:
            ans *= tmp_max
            ans %= mod
            r -= 2
        else:
            ans *= tmp_min
            ans %= mod
            l += 2
    return ans


(n, k) = map(int, input().split())
A = list(map(int, input().split()))
ans = solve(n, k, A)
print(ans)
