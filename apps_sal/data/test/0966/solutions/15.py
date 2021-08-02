import sys


def year():
    listyear = []
    year = input().split()
    k = True
    for i in range(len(year[0])):
        listyear.append(int(year[0][i]))
    listyear.reverse()
    return(listyear)


def nextyear(listyear):
    if listyear[0] == 9:
        listyear[0] = 0
        if listyear[1] == 9:
            listyear[1] = 0
            if listyear[2] == 9:
                listyear[2] = 0
                if listyear[3] == 9:
                    listyear[3] = 0
                else:
                    listyear[3] += 1
            else:
                listyear[2] += 1
        else:
            listyear[1] += 1
    else:
        listyear[0] += 1
    return listyear


def rightyear(listyear):
    nextyear(listyear)
    while len(set(listyear)) != 4:
        listyear = nextyear(listyear)
    listyear.reverse()

    for i in listyear:
        print(i, end="")


rightyear(year())
