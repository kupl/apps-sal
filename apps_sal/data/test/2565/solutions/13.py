t = int(input())

for i in range(t):
    x1, y1, z1 = list(map(int, input().split()))
    x2, y2, z2 = list(map(int, input().split()))
    ans = 0
    a = min(z1, y2)
    z1 -= a
    y2 -= a
    ans += 2 * a
    b = z2 - min(x1 + z1, z2)
    ans -= 2 * b
    print(ans)
