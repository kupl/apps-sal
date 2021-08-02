t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = a[-1] * a[-2] * a[-3] * a[-4] * a[-5]
    y = a[0] * a[1] * a[-1] * a[-2] * a[-3]
    z = a[0] * a[1] * a[2] * a[3] * a[-1]
    print(max(x, y, z))
