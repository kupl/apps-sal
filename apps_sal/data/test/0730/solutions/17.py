'''
Created on Oct 5, 2014

@author: Ismael
'''

def printBus(lastRow,otherRows):
    s = "+------------------------+\n"
    for i in range(4):
        s += "|"+lastRow[i]+"."
        for j in range(10):
            if(i == 2):
                s += ".."
            elif(i == 3):
                s += otherRows[j][i-1]+"."
            else:
                s += otherRows[j][i]+"."
        if(i == 0):
            s += "|D|)"
        elif(i == 1):
            s += "|.|"
        elif(i == 2):
            s += "..|"
        else:
            s += "|.|)"
        s += "\n"
    s += "+------------------------+"
    print(s)


def solve(n):
    lastRow = []
    otherRows = [[]]
    while(n>0):
        if(len(lastRow)<4):
            lastRow.append('O')
        else:
            if(len(otherRows[-1])<3):
                otherRows[-1].append('O')
            else:
                otherRows.append(['O'])
        n -= 1
    otherRows += [[] for _ in range(10-len(otherRows))]
    lastRow += (4-len(lastRow))*['#']
    for row in otherRows:
        row += (3-len(row))*['#']
    printBus(lastRow,otherRows)

n = int(input())
solve(n)
