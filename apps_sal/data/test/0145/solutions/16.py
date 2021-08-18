import math
import sys


def boyorgirl():
    distinct = []

    datain = input()

    for i in datain:
        if i not in distinct:
            distinct.append(i)

    if len(distinct) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


boyorgirl()
