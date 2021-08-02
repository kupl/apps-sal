#from IPython import embed

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def ffloor(a, b):
    if(b < 0): return ffloor(-a, -b);
    return a // b


def cceil(a, b):
    if(b < 0): return cceil(-a, -b);
    if a % b == 0:
        return a // b
    return a // b + 1;


def main():
    s = input()
    a1, b1, a2, b2, L, R = [int(i) for i in s.split()]

    if b2 < b1:
        a1, a2, b1, b2 = a2, a1, b2, b1

    d, x, y = xgcd(a1, -a2)  # extended_gcd(a1,-a2)
    if(d < 0):
        d *= -1
        x *= -1
        y *= -1

    if (b2 - b1) % d != 0:
        print(0)
        return

    # print(d,x,y)
    fact = (b2 - b1) // d
    x *= fact
    y *= fact

    c1 = a2 // d;
    c2 = a1 // d;

    tope1 = ffloor(R - b1 - a1 * x, a1 * c1);
    bajo1 = cceil(L - b1 - a1 * x, c1 * a1);
    bajo2 = cceil(L - b2 - a2 * y, c2 * a2);
    tope2 = ffloor(R - b2 - a2 * y, a2 * c2);

    bajo3 = max(cceil(-x, c1), cceil(-y, c2));

    bajo = max(bajo1, bajo2, bajo3);
    tope = min(tope1, tope2);
    print(max(0, tope + 1 - bajo))


    # embed()
main()
