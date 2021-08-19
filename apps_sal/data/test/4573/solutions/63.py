import copy


def main():
    N = int(input())
    X = [int(x) for x in input().split(' ')]
    sortedX = copy.deepcopy(X)
    sortedX.sort()
    cand = [sortedX[int(N / 2) - 1], sortedX[int(N / 2)]]
    for xi in X:
        if xi <= cand[0]:
            print(cand[1])
        else:
            print(cand[0])


main()
