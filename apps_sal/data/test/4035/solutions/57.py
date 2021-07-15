def main():
    A, B = tuple([int(_x) for _x in input().split()])
    for m in range(2000):
        if (m*108//100 - m) == A and (m*110//100 - m) == B:
            print(m)
            return
    print((-1))
    # N = int(input())


main()

