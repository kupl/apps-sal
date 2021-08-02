def main():
    import sys
    input = sys.stdin.readline

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    n, m, q = map(int, input().split())
    g = gcd(n, m)
    n //= g
    m //= g

    for i in range(q):
        s, x, t, y = map(int, input().split())
        x -= 1
        y -= 1
        if s == 1:
            x //= n
        else:
            x //= m
        if t == 1:
            y //= n
        else:
            y //= m
        if x == y:
            print("YES")
        else:
            print("NO")

    return 0


main()
