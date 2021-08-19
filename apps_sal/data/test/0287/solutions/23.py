(n, k) = map(int, input().split())
if k == 0 or k == n:
    print(0, 0)
else:
    c = n // 3
    m = n % 3
    if c >= k:
        print(1, k * 2)
    else:
        ans = c * 2
        if m == 2:
            ans += 1
            k -= 1
        elif m == 1:
            k -= 1
        ans -= k - c
        print(1, ans)
