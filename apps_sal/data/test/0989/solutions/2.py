n, k = list(map(int, input().split()))
a = sorted(map(int, input().split()))
i = 1
while True:
    ans = a[-i] - a[i - 1]
    if (a[i] - a[i - 1]) * i >= k:
        ans -= k // i
        break
    ans = a[-i] - a[i]
    k += a[i - 1] * i
    k -= a[i] * i
    if (a[-i] - a[-i - 1]) * i >= k:
        ans -= k // i
        break
    k += a[-i - 1] * i
    k -= a[-i] * i
    i += 1
    if not ans:
        break
print(ans)
