def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def main():
    (A, B, C, D) = map(int, input().split())
    E = lcm(C, D)
    (a_c, a_d, a_cd) = ((A - 1) // C, (A - 1) // D, (A - 1) // E)
    (b_c, b_d, b_cd) = (B // C, B // D, B // E)
    (a, b) = (a_c + a_d - a_cd, b_c + b_d - b_cd)
    ans = B - A + 1 - (b - a)
    print(ans)


main()
