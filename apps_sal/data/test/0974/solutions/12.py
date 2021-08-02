"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""
from sys import stdin, stdout


def main():
    n = int(stdin.readline().strip())
    a = [0 for i in range(n + 1)]

    top = -1
    reordered = 0
    toRemove = 1
    for x in range(n + n):
        cmmd = stdin.readline().strip()
        if cmmd[0] == 'a':
            k = int(cmmd.split(' ')[1])
            top += 1
            a[top] = k
        else:
            if toRemove == a[top] or top == -1:
                top = max(top - 1, -1)
            else:
                top = -1
                reordered += 1
            toRemove += 1

    stdout.write(str(reordered) + '\n')


def __starting_point():
    main()


__starting_point()
