t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    ans = 0
    for i in range(1, n):
        if b[0] < 0 and a[i] < 0:
            b.append(a[i])
        if b[0] > 0 and a[i] > 0:
            b.append(a[i])
        if b[0] < 0 and a[i] > 0:
            ans += max(b)
            b = [a[i]]
        if b[0] > 0 and a[i] < 0:
            ans += max(b)
            b = [a[i]]
    if len(b) >= 1:
        ans += max(b)
    print(ans)
