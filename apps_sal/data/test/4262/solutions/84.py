from itertools import permutations


def main():
    n = int(input())
    permutation = list(permutations([int(v) for v in range(1, n + 1)]))
    ans = 0
    first = tuple(int(v) for v in input().split())
    second = tuple(int(v) for v in input().split())
    firstNum = None
    secondNum = None
    for i in range(len(permutation)):
        if permutation[i] == first:
            firstNum = i + 1
        if permutation[i] == second:
            secondNum = i + 1
    ans = abs(firstNum - secondNum)
    return ans


def __starting_point():
    print(main())


__starting_point()
