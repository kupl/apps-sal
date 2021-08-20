def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [a[0]]
    for i in range(1, n):
        if gcd(a[i - 1], a[i]) != 1:
            b.append(1)
        b.append(a[i])
    print(len(b) - n)
    print(' '.join(map(str, b)))


main()
