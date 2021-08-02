n, k = list(map(int, input().split()))
ans = 1
k = min(k, n)
if k == 1:
    print(1)
elif k == 2:
    ans += n * (n - 1) // 2
    print(ans)
elif k == 3:
    ans += n * (n - 1) * (n - 2) // 3 + n * (n - 1) // 2
    print(ans)
else:
    ans += n * (n - 1) * (n - 2) * (n - 3) // 4 + n * (n - 1) * (n - 2) * (n - 3) // 8 + n * (n - 1) * (n - 2) // 3 + n * (n - 1) // 2
    print(ans)
