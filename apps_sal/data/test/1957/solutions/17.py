def readline():
    return tuple(map(int, input().split()))


def main():
    (n, a, b) = readline()
    (s1, *s) = readline()
    bound = s1 * (a - b) / b
    for si in sorted(s):
        bound -= si
        if bound < 0:
            break
        n -= 1
    print(n - 1)


main()
