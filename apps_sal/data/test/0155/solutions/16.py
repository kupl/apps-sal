def main():
    n, m, k = [int(i) for i in input().split(' ')]

    if k < n:
        print(k + 1, 1)
    else:
        k -= n
        m -= 1
        h1 = k // (2 * m) * 2
        h2 = k % (2 * m)
        if h2 < m:
            print(n - h1, 2 + h2)
        else:
            print(n - h1 - 1, 1 + m - h2 % m)


main()
