def main():
    n, b, a = map(int, input().split())
    cb, ca = b, a
    p = 0
    for s in input().split():
        if ca == 0 and cb == 0:
            break

        if int(s):
            if ca < a and cb > 0:
                ca += 1
                cb -= 1
            else:
                ca -= 1
        else:
            if ca > 0:
                ca -= 1
            else:
                cb -= 1
        p += 1

    print(p)


main()
