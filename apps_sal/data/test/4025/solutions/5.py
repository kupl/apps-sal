a = list(map(int, input().split()))
wek = min(a[0] // 3, a[1] // 2, a[2] // 2)
a[0] -= wek * 3
a[1] -= wek * 2
a[2] -= wek * 2
A = [0, 0, 1, 2, 0, 2, 1]
A = A + A
mx = 0
for i in range(7):
    ans = 0
    cur = i
    b = a.copy()
    while b[A[cur]]:
        ans += 1
        b[A[cur]] -= 1
        cur += 1
    mx = max(mx, ans)
print(mx + wek * 7)

