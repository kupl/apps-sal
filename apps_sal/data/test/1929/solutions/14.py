(n, t, c) = map(int, input().split())
(k, s) = (c - 1, 0)
for (i, j) in enumerate(map(int, input().split())):
    if j > t:
        s += max(0, i - k)
        k = i + c
print(s + max(0, n - k))
