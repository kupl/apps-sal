"""input
8 3
1 2 3 3 2 1 2 2
"""
(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
i = 1
if n == 1:
    print(1)
else:
    while i < n:
        t = 1
        while i < n and a[i] != a[i - 1]:
            t += 1
            i += 1
        i += 1
        ans = max(ans, t)
    print(ans)
