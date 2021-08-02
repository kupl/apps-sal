def main() -> int:
    n = int(input()) + 1
    fingers = [int(word) for word in input().split()]
    sum_fingers = sum(fingers)
    count = 0

    for i in range(sum_fingers + 1, sum_fingers + 6, 1):
        if i % n == 1:
            count += 1

    result = 5 - count
    print(result)

    return 0


def __starting_point():
    main()


__starting_point()
