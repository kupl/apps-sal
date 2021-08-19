tc = int(input())
for ii in range(tc):
    (n, m) = list(map(int, input().split()))
    ar = list(map(int, input().split()))
    if m < n or n == 2:
        print(-1)
        continue
    ans = 0
    mn1 = float('inf')
    for i in range(n):
        ans += ar[i] * 2
        if ar[i] < mn1:
            save1 = i
            mn1 = ar[i]
    m -= n
    mn2 = float('inf')
    for i in range(n):
        if ar[i] < mn2 and i != save1:
            mn2 = ar[i]
            save2 = i
    ans += m * (mn1 + mn2)
    print(ans)
    for i in range(m):
        print(save1 + 1, save2 + 1)
    for i in range(n):
        print(i + 1, (i + 1) % n + 1)
