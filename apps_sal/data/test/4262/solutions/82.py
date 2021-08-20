import math
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


def getIndex(target):
    rtn = 0
    n_list = [i for i in range(1, N + 1)]
    for p in target:
        index = n_list.index(p)
        del n_list[index]
        rtn += math.factorial(len(n_list)) * index
    return rtn


print(abs(getIndex(P) - getIndex(Q)))
