t = int(input())
for i in range(t):
    s = input().split()
    n, a, b = int(s[0]), int(s[1]), int(s[2])
    x = min(a * 2, b)
    d = n // 2
    res = d * x
    n -= 2 * d
    if n != 0:
        res += a
    print(res)
