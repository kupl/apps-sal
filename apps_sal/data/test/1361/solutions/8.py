def main():
    n = int(input())
    aa = list(map(int, input().split()))
    bb = [b - a for b, a in zip(aa[1:], aa)]
    print(max(min(a + b for a, b in zip(bb[1:], bb)), max(bb)))


def __starting_point():
    main()


__starting_point()
