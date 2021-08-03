n, k = map(int, input().split())
if k % 2 == 1:
    print((n // k)**3)
else:
    ans = (n // k)**3
    ans += (n // (k // 2) - n // k)**3
    print(ans)
