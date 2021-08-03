def a(x):
    n_e = 0
    n_o = 0
    for a in x:
        if a % 2 == 1:
            n_o += 1
        else:
            n_e += 1
    return (n_o, n_e)


T = int(input())
for _ in range(T):
    r, g, b, w = list(map(int, input().split()))
    z = a([r, g, b, w])
    if z[0] <= 1:
        print("Yes")
        continue
    elif r >= 1 and g >= 1 and b >= 1:
        w += 1
        r -= 1
        g -= 1
        b -= 1
        z = a([r, g, b, w])
        if z[0] <= 1:
            print("Yes")
            continue
    print("No")
