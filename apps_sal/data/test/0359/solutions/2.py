def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


def main():
    a, h, w = map(int, input().split())
    x = gcd(a + h, a + w)
    y = (a + w) // x
    z = ((w // a + 1) // y) * y - 1
    if(z <= 0):
        print("-1")
    else:
        print("%.10lf" % ((1.00 * w - z * a) / (z + 1)))


main()
