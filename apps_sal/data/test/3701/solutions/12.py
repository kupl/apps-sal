def main():
    n, x, y = list(map(int, input().split()))
    s, zo, a = input(), [0, 0], ' '
    for b in s:
        if a != b:
            zo[b == '1'] += 1
            a = b
    z, o = zo
    if s[0] == '1':
        o -= 1
    if s[-1] == '1':
        o -= 1
    if o < 0:
        o = 0
    print(min(z * y, o * x + y))


def __starting_point():
    main()

__starting_point()
