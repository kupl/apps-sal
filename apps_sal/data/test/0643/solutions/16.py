R = lambda: map(int, input().split())
mx = 10**9 + 7
t = int(input())
for i in range(t):
    a, b, p, q = R()
    l, r = 1, mx
    while l < r:
        k = (l + r) // 2
        x, y = k * p - a, k * q - b
        if 0 <= x <= y and y >= 0:
            r = k
        else:
            l = k + 1
    if r >= mx:
        print("-1")
    else:
        print(r * q - b)
