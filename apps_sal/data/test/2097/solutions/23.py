def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = [int(x) for x in input().strip().split()]
        zeros = 0
        sum_ = sum(array)
        for x in array:
            if x == 0:
                zeros += 1
        if (zeros + sum_) == 0:
            zeros += 1
        print(zeros)


def __starting_point():
    main()


__starting_point()
