n = int(input())
tab = list(map(int, input().split()))
tab = sorted(tab, reverse=True)
maxi = 0
tmpOdd = 0
maxOdd = 0
oddFirst = True
for i in tab:
    if i % 2 == 0 and i > 0:
        maxi += i
    elif i % 2 == 1:
        tmpOdd += i
        if tmpOdd % 2 == 1:
            if maxOdd < tmpOdd or oddFirst:
                oddFirst = False
                maxOdd = tmpOdd
maxi += maxOdd
print(maxi)
