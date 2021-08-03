def cost(n, arr, x):
    tot = 0
    for i in range(n):
        tot += (abs(x - i) + i + x) * arr[i]
    return tot * 2


def prog():
    n = int(input())
    arr = [int(x) for x in input().split()]
    currcost = 10**18
    for i in range(n):
        currcost = min(currcost, cost(n, arr, i))
    return currcost


print(prog())
