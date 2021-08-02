import bisect
n = int(input())
s = [*map(int, input().split())]
s.sort()
t = [a - b for a, b in zip(s[1:], s)] + [100000000000000000000]
t.sort()
S = [0]
for i in range(n): S += [S[-1] + t[i]]
R = []
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    L = r - l + 1
    j = bisect.bisect_left(t, L)
    R += [S[j] + (n - j) * L]
print(' '.join(map(str, R)))
