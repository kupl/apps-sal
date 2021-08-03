def main():
    n, m = map(int, input().split())
    if 2 * m < n:
        if m == 0:
            print(1)
        else:
            print(m)
    else:
        print(n - m)
    return 0


main()
