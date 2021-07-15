n, a, b = map(int, input().split())
dancers = list(map(int, input().split()))
ans = 0
real = True
for i in range(n):
    if dancers[i] == 2:
        if dancers[n - i - 1] == 2:
            ans += min(a, b)
        elif dancers[n - i - 1] == 0:
            ans += a
        else:
            ans += b
    elif dancers[i] != dancers[n - i - 1] and dancers[n - i - 1] != 2:
        real = False
        break
if real:
    print(ans)
else:
    print(-1)
