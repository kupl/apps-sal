def main():
    def calc(x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0
        if (x2 - x1 + 1) * (y2 - y1 + 1) % 2 == 0:
            return (x2 - x1 + 1) * (y2 - y1 + 1) // 2
        if (x1 + y1) % 2 == 1:
            return (x2 - x1 + 1) * (y2 - y1 + 1) // 2 + 1
        return (x2 - x1 + 1) * (y2 - y1 + 1) // 2
    T = int(input())
    for t in range(T):
        n, m = list(map(int, input().split()))
        a, b, c, d = list(map(int, input().split()))
        e, f, g, h = list(map(int, input().split()))
        j, k, l, q = max(a, e), max(b, f), min(c, g), min(d, h)
        black = calc(1, 1, n, m) - calc(a, b, c, d) - calc(e, f, g, h) + (h - f + 1) * (g - e + 1) + calc(j,k,l,q)
        print(n * m - black, black)

main()

