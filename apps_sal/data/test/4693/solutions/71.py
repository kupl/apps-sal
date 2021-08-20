def LI():
    return list(map(int, input().split()))


(A, B) = LI()


def main():
    ans = A + B
    if ans >= 10:
        ans = 'error'
    print(ans)


def __starting_point():
    main()


__starting_point()
