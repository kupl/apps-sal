t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = ['0'] * n
    ans[0] = '1'
    ans[-1] = '1'
    l = 0
    r = n - 1
    now = n
    while (r - l) > 1:
        if a[r] > now:
            r -= 1
            continue
        if a[l] > now:
            l += 1
            continue
        if (r - l + 1) == now:
            ans[r - l] = '1'
        now -= 1
    if (r - l  + 1) == now:
        ans[r - l] = '1'
    print(''.join(ans))



