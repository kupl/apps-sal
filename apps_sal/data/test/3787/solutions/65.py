import math
(n, a, b) = map(int, input().split())
f = 1
ans = [0] * n
if max(a, b) > n:
    f = 0
elif not math.ceil((n - a) / a) + 1 <= b <= n - a + 1:
    f = 0
if f:
    ans[-a] = 1
    if not b == 1:
        (c, d) = ((n - a) // (b - 1), b - 1 - (n - a) % (b - 1))
        now = n + 1
        i = 0
        for j in range(b - 1):
            now -= c
            if j >= d:
                now -= 1
            ans[i] = now
            i += c
            if j >= d:
                i += 1
    for i in range(1, n):
        if ans[i] == 0:
            ans[i] = ans[i - 1] + 1
print(' '.join(map(str, ans)) if f else -1)
