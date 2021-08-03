def main():
    n, a, b = list(map(int, input().split()))
    t = a + b
    s = input()
    last = -1
    for c in s:
        if c == '.':
            if last == -1:
                if a >= b and a > 0:
                    last = 0
                    a -= 1
                elif b >= a and b > 0:
                    last = 1
                    b -= 1
            elif last == 0 and b > 0:
                last = 1
                b -= 1
            elif last == 1 and a > 0:
                last = 0
                a -= 1
            else:
                last = -1
        else:
            last = -1

    print(t - a - b)


main()
