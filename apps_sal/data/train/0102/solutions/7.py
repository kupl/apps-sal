q = int(input())
while q:
    a = int(input())
    g = len(str(a))
    ans = (g - 1)*9
    h = (pow(10, g) - 1)/9
    x = h
    while a - (x + h) >= 0:
        x += h
    ans += int(str(x)[0])
    if x > a:
        ans -= 1
    print(ans)
    q -= 1

