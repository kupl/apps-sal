t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    ans = n * (k // (n - 1))
    if k % (n - 1) == 0:
        ans -= 1
    else:
        ans += k % (n - 1)

    print(ans)
