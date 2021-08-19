def main():
    A = list(map(int, input().split()))
    K = int(input())
    A.sort()
    A.append(A.pop() * 2 ** K)
    print(sum(A))


def __starting_point():
    main()


__starting_point()
