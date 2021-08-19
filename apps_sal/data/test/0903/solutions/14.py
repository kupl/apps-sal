(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
x = len(a) // 2
rem = 1
ans = a[x]
while k > 0:
    if x + rem < len(a):
        if k >= rem * (a[x + rem] - a[x + rem - 1]):
            k -= rem * (a[x + rem] - a[x + rem - 1])
            ans = a[x + rem]
            rem += 1
        else:
            ans += k // rem
            k = 0
    else:
        ans += k // rem
        k = 0
print(ans)
