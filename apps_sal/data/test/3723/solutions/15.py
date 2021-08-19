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
        #count = sum(nums[i:n+1:i])
        highestCount = max(highestCount, count)
    return highestCount
    # for j in range(i, n + 1, i):
    #	count +=

    # n = max(L)
    # primes = makePrimes(n)
    # highestCount = maxCount(L)
    # for prime in primes:
    # 	if prime > n**0.5:
    # 		break
    # 	count = len([x for x in L if x % prime == 0])
    # 	if count > highestCount:
    # 		highestCount = count
    # return highestCount


def maxCount(L):
    d = dict()
    for x in L:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    d[1] = 1
    return max([d[x] for x in d])

# print(solver([2, 3, 4]))
# print(solver([3, 9]))
# print(solver([2, 3, 4, 6, 7]))
# print(solver([12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 12553, 15, 1, 18, 28, 20, 6, 31, 16, 5, 23, 21, 38, 3, 11, 18, 11, 3, 25, 33]))
# print(solver([1, 1, 1]))
# print(solver([1, 3, 6]))


main()
