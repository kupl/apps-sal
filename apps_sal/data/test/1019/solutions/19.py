def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    n = int(input())
    res = (0, 1)

    for i in range(1, n):
        a, b = i, n - i
        if b <= a:
            break
        g = gcd(a, b)
        if g != 1:
            continue
        if a * res[1] > b * res[0]:
            res = (a, b)

    print(res[0], res[1])


main()
