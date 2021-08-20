import sys


def solve(n, m, k, a):
    if m == 1:
        if k == n:
            return sum(a)
        else:
            return sum(sorted(a, reverse=True)[:k])
    r0 = m + 0 - 1
    sum0 = sum(a[:r0 + 1])
    s = [sum0]
    for i in range(r0 + 1, n):
        sum0 = sum0 + a[i] - a[i - m]
        s.append(sum0)
    t = [0] * len(s)
    t[0] = s[0]
    for i in range(1, len(s)):
        t[i] = max(s[i], t[i - 1])
    for i in range(1, k):
        nt = [0] * len(s)
        for j in range(i * m, len(s)):
            nt[j] = t[j - m] + s[j]
            nt[j] = max(nt[j], nt[j - 1])
        t = nt
    return t[-1]


(n, m, k) = list(map(int, sys.stdin.readline().strip().split()))
numbers = list(map(int, sys.stdin.readline().strip().split()))
r = solve(n, m, k, numbers)
print(r)
