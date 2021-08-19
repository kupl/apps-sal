(n, a, b) = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
for i in range(n // 2):
    if c[i] == 2 and c[n - i - 1] == 2:
        ans += min(a, b) * 2
    elif c[i] == 2:
        if c[n - i - 1] == 0:
            ans += a
        else:
            ans += b
    elif c[n - i - 1] == 2:
        if c[i] == 0:
            ans += a
        else:
            ans += b
    elif c[i] != c[n - i - 1]:
        print(-1)
        break
else:
    if n % 2:
        ans += (c[n // 2] == 2) * min(a, b)
    print(ans)
