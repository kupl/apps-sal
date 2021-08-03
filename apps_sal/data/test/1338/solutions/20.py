def rek(s, t):
    nonlocal q, n
    for x in range(t + 1, n + 1):
        y = s[:n - x] + s[n - x:][::-1]
        q.append(y)
        rek(y, x)


n, m = map(int, input().split())
a = ''.join(map(str, range(1, n + 1)))
q = [a]
rek(a, 1)
q.sort()
print(' '.join(q[m - 1]))
