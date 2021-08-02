import sys


def main():
    left = 0
    right = int(input()) - 1
    arr = [int(k) for k in input().split()]
    score = [0, 0]
    i = 0

    while left != right:
        if arr[left] > arr[right]:
            score[i] += arr[left]
            left += 1
        else:
            score[i] += arr[right]
            right -= 1
        i += 1
        i %= 2

    score[i] += arr[left]
    print(score[0], score[1])


def __starting_point():
    main()


__starting_point()
