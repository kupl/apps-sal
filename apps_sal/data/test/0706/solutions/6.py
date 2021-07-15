def poll(a, k):
    if k == 1:
        return a
    if k % 2 == 1:
        return poll(a * a % 1000000007, k // 2) * a % 1000000007
    return poll(a * a % 1000000007, k // 2)

a, b, n, x = [int(i) for i in input().split()]
if a != 1:
    r = poll(a, n)
    rr = r - 1
    rr *= poll((a - 1), 1000000005)
    rr *= b
    r *= x
    print((r + rr) % 1000000007)
else:
    r = x + b * n
    print(r % 1000000007)
