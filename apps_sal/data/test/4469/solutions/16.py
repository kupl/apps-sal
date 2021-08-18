'''input
10
L 100
R 100000
R 123
L 101
? 123
L 10
R 115
? 100
R 110
? 115
'''
from sys import stdin, stdout


def myfunction(mydict, current, second):
    a = mydict[second]
    if a[2] == 'R':
        return min(current[1] - a[1], current[0] + a[1] - 1)
    else:
        return min(current[0] - a[0], current[1] + a[0] - 1)


q = int(stdin.readline())
mydict = dict()
current = [0, 0, 0]

while q > 0:

    first, second = stdin.readline().split()
    if first == 'L':
        mydict[second] = [current[0] + 1, current[1], 'L']
        current = [current[0] + 1, current[1], 'L']
    elif first == 'R':
        mydict[second] = [current[0], current[1] + 1, 'R']
        current = [current[0], current[1] + 1, 'R']
    else:
        print(myfunction(mydict, current, second))

    q -= 1
