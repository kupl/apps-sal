def main():
    n, s = list(map(int, input().split()))

    g = [0 for _ in range(n)]
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        g[a] += 1
        g[b] += 1

    m = 0
    for x in g:
        if x == 1:
            m += 1

    print(2 * s / m)


main()
