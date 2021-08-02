import math


def lcm(a, b):
    g = math.gcd(max(a, b), min(a, b))
    return a * b // g


def main():
    x = int(input())
    facts = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            facts.append([i, x // i])

    min_val = float('inf')
    a = -1
    b = -1
    for i in facts:
        if max(i) < min_val and lcm(i[0], i[1]) == x:
            min_val = max(i)
            a = i[0]
            b = i[1]

    print(a, b)


main()
