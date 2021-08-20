n = int(input())
for _ in range(n):
    a = sorted(list(map(int, input().split())))
    (a, b, c) = (a[2], a[1], a[0])
    ans = 0
    if a:
        ans += 1
        a -= 1
    if b:
        ans += 1
        b -= 1
    if c:
        ans += 1
        c -= 1
    if a > 0 and b > 0:
        ans += 1
        a -= 1
        b -= 1
    if b > 0 and c > 0:
        ans += 1
        b -= 1
        c -= 1
    if a > 0 and c > 0:
        ans += 1
        a -= 1
        c -= 1
    if a > 0 and b > 0 and (c > 0):
        ans += 1
    print(ans)
