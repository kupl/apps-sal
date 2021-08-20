(n, m) = list(map(int, input().split()))
t = m
if m >= n - 1:
    print(n - 1)
else:
    for i in range(2, n - m + 1):
        t = t + i
    print(t)
