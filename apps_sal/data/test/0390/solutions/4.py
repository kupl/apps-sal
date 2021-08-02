n, w, b = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n // 2):
    if a[i] == 1:
        if a[n - 1 - i] == 2:
            ans += b
        elif a[n - 1 - i] == 0:
            print(-1)
            return
    elif a[i] == 0:
        if a[n - 1 - i] == 2:
            ans += w
        elif a[n - 1 - i] == 1:
            print(-1)
            return
    else:
        if a[n - 1 - i] == 1:
            ans += b
        elif a[n - 1 - i] == 0:
            ans += w
        else:
            ans += 2 * (min(w, b))
if n % 2 and a[n // 2] == 2:
    ans += min(w, b)
print(ans)
