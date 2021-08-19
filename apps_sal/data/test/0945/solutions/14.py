"""
Created on Oct 31, 2013

@author: Ismael
"""


def main():
    input()
    l = list(map(int, input().split()))
    if len(l) <= 3:
        print('no')
        return
    xMin = min(l[0], l[1])
    xMax = max(l[0], l[1])
    for i in range(2, len(l) - 1):
        if l[i] <= xMin or l[i] >= xMax:
            if l[i + 1] > xMin and l[i + 1] < xMax:
                print('yes')
                return
        elif l[i] >= xMin and l[i] <= xMax:
            if l[i + 1] < xMin or l[i + 1] > xMax:
                print('yes')
                return
        min123 = min(xMin, l[i])
        max123 = max(xMax, l[i])
        if l[i + 1] < min123 or l[i + 1] > max123:
            xMin = min123
            xMax = max123
        else:
            elems = [l[i + 1], xMin, xMax, l[i]]
            elems.sort()
            ind4 = elems.index(l[i + 1])
            xMin = elems[ind4 - 1]
            xMax = elems[ind4 + 1]
    print('no')


main()
