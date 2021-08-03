n, k, t = list(map(int, input().split()))
if (t <= k):
    print(t)
else:
    if (t <= n):
        print(k)
    else:
        print(n + k - t)
