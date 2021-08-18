import numpy as np
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers = np.array(numbers)
    count = 0

    if np.all(numbers % 2 == 1):
        print(0)
        return
    while True:
        if np.all(numbers % 2 == 1) == True:
            break
        else:
            idx = np.where(numbers % 2 == 0)
            count += np.count_nonzero(numbers % 2 == 0)
            numbers[idx] = numbers[idx] // 2
    print(count)


def __starting_point():
    main()


__starting_point()
