__author__ = 'markdaniel'


def main():
    num1, num2 = [int(x) for x in input().split(' ')]
    maxval = max(num1, num2)
    minval = min(num1, num2)
    ops = 0
    while maxval > 0 and minval > 0:
        remainderMultiple = ((maxval - minval) // minval)
        maxval -= remainderMultiple * minval
        ops += remainderMultiple
        maxval -= minval
        ops += 1
        if maxval < minval:
            temp = maxval
            maxval = minval
            minval = temp

    return ops


def __starting_point():
    cases = int(input())
    for i in range(cases):
        print(main())


__starting_point()
