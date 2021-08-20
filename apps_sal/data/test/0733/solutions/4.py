def gcd(x, y):
    if y % x == 0:
        return x
    else:
        return gcd(y % x, x)


def __starting_point():
    inp = input()
    arr = inp.split(' ')
    x = int(arr[0])
    y = int(arr[1])
    a = int(arr[2])
    b = int(arr[3])
    g = gcd(min(x, y), max(x, y))
    l = x * y // g
    i = 0
    for i in range(a, a + l + 1):
        if i > b:
            break
        if i % l == 0:
            break
    ans = 0
    if b >= i:
        ans = (b - i) // l + 1
    print(ans)


__starting_point()
