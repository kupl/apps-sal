# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    steps = []
    step_data = []
    step = int(input())
    steps = list(map(int, input().split()))
    count = 0

    for idx in range(1, len(steps)):
        if steps[idx - 1] >= steps[idx]:
            count += 1
        else:
            step_data.append(count)
            count = 0
    step_data.append(count)
    print(max(step_data))


def __starting_point():
    main()


__starting_point()
