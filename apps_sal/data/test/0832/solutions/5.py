import sys
import math


def games():
    datain = []
    shirts = 0
    homeshirts = []
    awayshirts = []

    teams = int(input())
    for i in range(teams):
        datain.append(input().split())

    for i in range(teams):
        homeshirts.append(datain[i][0])

    for i in range(teams):
        awayshirts.append(datain[i][1])

    for i in homeshirts:
        shirts += awayshirts.count(i)

    print(shirts)


games()
