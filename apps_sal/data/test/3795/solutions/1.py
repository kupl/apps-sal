def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    d = int(input())
    e = int(input()) * 5

    mi = n
    i = 0
    while i * e <= n:
        mi = min(mi, (n - i * e) % d)
        i += 1

    print(mi)

    return 0


main()
