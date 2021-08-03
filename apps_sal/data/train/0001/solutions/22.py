q = int(input())
for i in range(q):
    n, m, k = map(int, input().split())
    ans = max(n, m)
    diff = k - ans
    if diff < 0:
        print(-1)
    else:
        if (n % 2 == 0 and m % 2 == 0) or (n % 2 != 0 and m % 2 != 0):
            if diff % 2 == 0:
                ans += diff
            else:
                ans += diff - 2
        else:
            ans += diff - 1
        print(ans)
