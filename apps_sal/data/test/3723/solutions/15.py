def main():
    n = input()
    L = [int(x) for x in input().split()]
    print(solver(L))


def solver(L):
    n = max(L)
    nums = [0] * (n + 1)
    for x in L:
        nums[x] += 1
    highestCount = 1
    for i in range(2, n + 1):
        count = 0
        for j in range(i, n + 1, i):
            count += nums[j]
        highestCount = max(highestCount, count)
    return highestCount


def maxCount(L):
    d = dict()
    for x in L:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    d[1] = 1
    return max([d[x] for x in d])


main()
