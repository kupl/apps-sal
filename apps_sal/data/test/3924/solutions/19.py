n, k = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
a.append(0)
ans = 0
for i in range(1, n + 2):
    t = (a[i - 1] + a[i]) // k
    if t > 0:
        ans += t
        t = (t * k) - a[i - 1]
        a[i] -= t
    else:
        if a[i - 1] > 0:
            ans += 1
            a[i] = 0
print(ans)

