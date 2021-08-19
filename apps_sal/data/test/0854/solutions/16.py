n, t = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

while True:
    b = False
    k = 0
    s = 0
    for i in range(n):
        if t >= a[i]:
            s += a[i]
            k += 1
            b = True
    if not(b):
        break
    if t < s:
        for i in range(n):
            if t >= a[i]:
                ans += 1
                t -= a[i]
    else:
        ans += (t // s) * k
        t %= s
    #print(ans, t, s)
print(ans)
