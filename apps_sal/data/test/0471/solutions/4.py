(n, a) = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
if n == 1:
    print(0)
elif n == 2:
    print(min(abs(c[0] - a), abs(c[1] - a)))
else:
    if abs(c[0] - a) < abs(c[n - 2] - a):
        ans = abs(c[0] - a) + abs(c[0] - c[n - 2])
    else:
        ans = abs(c[n - 2] - a) + abs(c[0] - c[n - 2])
    if abs(c[1] - a) < abs(c[n - 1] - a):
        ans = min(ans, abs(c[1] - a) + abs(c[1] - c[n - 1]))
    else:
        ans = min(ans, abs(c[n - 1] - a) + abs(c[n - 1] - c[1]))
    print(ans)
