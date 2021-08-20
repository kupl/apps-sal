def main():
    (n, m, k, l) = map(int, input().split())
    d = (l + k) // m
    if (l + k) % m:
        d += 1
    if m * d > n or n - k < l:
        print(-1)
    else:
        print(d)


main()
