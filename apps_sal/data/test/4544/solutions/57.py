

def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = [0] * 100002
    ans = 0

    for a in A:
        if a != 0:
            B[a - 1] += 1
        B[a] += 1
        B[a + 1] += 1

    ans = max(B)

    print(ans)


def __starting_point():
    main()


__starting_point()
