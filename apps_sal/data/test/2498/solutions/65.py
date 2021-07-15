def abc150_d():
    n, m = (int(x) for x in input().split())
    A = [int(x) // 2 for x in input().split()]

    from math import gcd
    def lcm(a, b):
        return a * b // gcd(a, b)

    x = 1
    for a in A:
        x = lcm(x, a)

    valid = True
    for a in A:
        if (x // a) % 2 == 0:
            valid = False
            break

    if valid: ans = (m // x + 1) // 2
    else: ans = 0
    print(ans)

def __starting_point():
    abc150_d()
__starting_point()
