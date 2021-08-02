t = int(input())
for q in range(t):
    a = list(map(int, input().split()))
    ans = 0
    for i in range(3):
        if a[i] > 0:
            ans += 1
            a[i] -= 1
    a.sort()
    a.reverse()
    if a[0] and a[1]:
        a[0] -= 1
        a[1] -= 1
        ans += 1
    if a[0] and a[2]:
        a[0] -= 1
        a[2] -= 1
        ans += 1
    if a[1] and a[2]:
        a[1] -= 1
        a[2] -= 1
        ans += 1
    if a[0] and a[1] and a[2]:
        ans += 1
    print(ans)
