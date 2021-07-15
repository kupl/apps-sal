import sys

n = int(input())
nums = list(map(int, input().split()))
eleCount = {}
possibleMax = 1
for i in range(n):
    if nums[i] in list(eleCount.keys()):
        eleCount[nums[i]] += 1
        if len(list(eleCount.keys())) == 1:
            possibleMax = i+1
        else:
            x = list(eleCount.values())
            x.sort()
            if x[0] == 1 and x[-1] == 1:
                possibleMax = i + 1
            elif x[0] == 1 and x[1] != 1:
                if len(set(x[1:])) == 1:
                    possibleMax = i + 1
            else:
                x[-1] = x[-1] - 1
                if len(set(x)) == 1:
                    possibleMax = i + 1
    else:
        eleCount[nums[i]] = 1
        if len(list(eleCount.keys())) == 1:
            possibleMax = i+1
        else:
            x = list(eleCount.values())
            x.sort()
            if x[0] == 1 and x[-1] == 1:
                possibleMax = i + 1
            elif x[0] == 1 and x[1] != 1:
                if len(set(x[1:])) == 1:
                    possibleMax = i + 1
            else:
                x[-1] = x[-1] - 1
                if len(set(x)) == 1:
                    possibleMax = i + 1
print(possibleMax)

