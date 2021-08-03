n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

rt = -1

ap = [a[0]]

for i in range(1, n):
    ap.append(ap[i - 1] + a[i])

for ki in range(k, n + 1):
    ans = -1
    for i in range(n - ki + 1):

        if i + ki - 1 < n:
            if i > 0:
                ans = max(ans, (ap[i + ki - 1] - ap[i - 1]))
            else:
                ans = max(ans, ap[i + ki - 1])

    rt = max(rt, ans / ki)

print(rt)
