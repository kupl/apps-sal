candies = int(input())


def printCandies(touse):
    print(len(result))
    resultS = ""
    for child in touse:
        resultS += str(child) + " "
    print(resultS)


if candies >= 1 and candies <= 1000:
    result = []
    for i in range(1, candies + 1):
        result.append(i)
        if sum([int(i) for i in result]) > candies:
            result = result[0:-1]
            break
    sumN = sum(result)
    if sumN == candies:
        printCandies(result)
    else:
        remain = candies - sum(result)

        for i in range(remain, 0, -1):
            result[-1 - (i - 1)] += 1

        printCandies(result)
