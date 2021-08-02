s = "RGB" * 666
rgb = ["GB" + s]
rgb.append("RGB" + s)
rgb.append("BRGB" + s)
for _ in range(int(input())):
    n, k = map(int, input().split())
    t = input()
    l = len(t)
    ans = 2001
    a = [0] * l
    for i in range(3):
        a[0] = 1 if rgb[i][0] != t[0] else 0
        for j in range(1, l):
            a[j] = a[j - 1] + (1 if rgb[i][j] != t[j] else 0)
        ans = min(ans, a[k - 1])
        for j in range(k, l):
            ans = min(ans, a[j] - a[j - k])
    print(ans)
