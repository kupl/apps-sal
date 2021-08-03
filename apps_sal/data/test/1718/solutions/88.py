n, k = list(map(int, input().split()))
ans = (n - 1) // (k - 1)
if (n - 1) % (k - 1) == 0:
    print(ans)
else:
    print((ans + 1))
