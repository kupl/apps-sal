n, a, b = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
if n % 2 != 0 and c[n // 2] == 2:
    ans += min(a, b)
for i in range(n // 2):
    if c[i] == c[n - i - 1]:
        if c[i] == 2:
            ans += 2 * (min(a, b))
    else:
        if c[i] == 1 and c[n - i - 1] == 2 or c[i] == 2 and c[n - i - 1] == 1:
            ans += b
        elif c[i] == 0 and c[n - i - 1] == 2 or c[i] == 2 and c[n - i - 1] == 0:
            ans += a
        else:
            print(-1)
            return()
print(ans)
