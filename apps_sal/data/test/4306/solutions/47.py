def main():
    A, B, C, D = list(map(int, input().split()))

    if D <= A or B <= C:
        ans = 0
    if C <= A and A <= D:
        ans = D - A
    if C <= B and B <= D:
        ans = B - C
    if A <= C and D <= B:
        ans = D - C
    if C <= A and B <= D:
        ans = B - A
    print(ans)


def __starting_point():
    main()


__starting_point()
