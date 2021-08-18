import sys


def prefix(s):
    m = len(s)
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i - 1]
        while k > 0 and s[k] != s[i]:
            k = v[k - 1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    w = set()
    i = m - 1
    while v[i] != 0:
        w.add(m - v[i])
        i = v[i] - 1

    return w


n, m = list(map(int, input().split()))
if m == 0:
    print(pow(26, n, 1000000007))
    return
p = input()
l = len(p)
x = list(map(int, input().split()))
w = prefix(p)
busy = l
for i in range(1, m):
    if x[i] - x[i - 1] < l and (x[i] - x[i - 1]) not in w:
        print(0)
        return
    busy += min(x[i] - x[i - 1], l)

print(pow(26, n - busy, 1000000007))
