L1 = list(map(int, input().split()))
numList = list(map(int, input().split()))
length = L1[0]
m = L1[1]


def greaterCount(numList, m):
    countDic = {0: 1}
    sum = 0
    total = 0
    rem = 0
    for number in numList:
        if number >= m:
            sum += 1
            rem += countDic[sum - 1]
            total += rem
        else:
            sum -= 1
            if sum in countDic:
                rem -= countDic[sum]
            total += rem

        if sum in countDic:
            countDic[sum] += 1
        else:
            countDic[sum] = 1

    #print("m=", m, "number=", number, "sum=", sum, "total=", total, "rem=", rem, "countDic=", countDic)
    return total


print(greaterCount(numList, m) - greaterCount(numList, m + 1))
