(a, b, c) = (int(z) for z in input().split())


def f(a, b, c):
    x = 0
    ca = c // a
    res = 0
    while x <= ca:
        if (c - res) % b == 0:
            return 'Yes'
        else:
            res += a
            x += 1
    return 'No'


print(f(a, b, c))
