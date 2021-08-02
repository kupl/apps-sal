def pattern1(A, B):
    s1 = (A // 3) * B
    s2 = ((A - (A // 3)) // 2) * B
    s3 = A * B - s1 - s2
    return max([abs(s1 - s2), abs(s2 - s3), abs(s3 - s1)])


def pattern2(A, B):
    a1 = A // 2
    a2 = A - a1
    b1 = (2 * B + 1) // 3
    b2 = B - b1
    s1, s2, s3 = a1 * b1, a2 * b1, A * b2
    return max([abs(s1 - s2), abs(s2 - s3), abs(s3 - s1)])


def main():
    H, W = list(map(int, input().split(' ')))
    ans = min([
        pattern1(H, W),
        pattern1(W, H),
        pattern2(H, W),
        pattern2(W, H)
    ])
    print(ans)


def __starting_point():
    main()


__starting_point()
