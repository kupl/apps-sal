def f(b, n):
    if n < b:
        return n
    return f(b, n // b) + n % b


N = int(input())
S = int(input())


def factors(n):
    ans = []
    cur = 1
    while cur * cur <= n:
        if n % cur == 0:
            ans.append(cur)
            if cur * cur != n:
                ans.append(n // cur)
        cur += 1
    return ans


MAX_S = 5 * 10 ** 5


def solve(n, s):
    b = 2
    while b * b <= n:
        if f(b, n) == s:
            return b
        b += 1
    if n < s:
        return -1
    if n == s:
        return n + 1
    facs = factors(n - s)
    for fac in sorted(facs):
        b = fac + 1
        if b * b <= n:
            continue
        alpha = (n - s) // fac
        beta = s - alpha
        if alpha >= 0 and alpha < b and (beta >= 0) and (beta < b):
            return b
    return -1


print(solve(N, S))
