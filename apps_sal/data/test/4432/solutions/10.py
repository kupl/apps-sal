t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    index = 0
    now = a[0]
    mx = a[0]
    while index < n:
        while index < n and now * a[index] > 0:
            mx = max(mx, a[index])
            index += 1
        ans += mx
        if index == n:
            break
        now = a[index]
        mx = a[index]
    print(ans)

