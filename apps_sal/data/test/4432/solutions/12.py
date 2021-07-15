t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ind = 0
    ans = 0
    while ind < n:
        cur = -10000000001
        if a[ind] < 0:
            while ind < n and a[ind] < 0:
                cur = max(a[ind], cur)
                ind += 1
        else:
            while ind < n and a[ind] > 0:
                cur = max(a[ind], cur)
                ind += 1
        ans += cur
    print(ans)
