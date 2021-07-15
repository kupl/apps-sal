t = int(input())
for i in range(t):
    n = int(input())
    s = str(n)
    l = len(s)
    x = int(s[0])
    nm = int(str(x)*l)
    if n - nm < 0:
        x -= 1
    print((l - 1) * 9 + x)
