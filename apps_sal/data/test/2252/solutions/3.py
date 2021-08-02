"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""
from sys import stdin, stdout


def main():
    n, m = [int(_) for _ in input().split()]
    p = [int(_) for _ in input().split()]

    for i in range(m):
        l, r, x = [int(_) for _ in input().split()]
        l -= 1
        r -= 1
        x -= 1
        val = p[x]

        smaller = 0
        for j in range(l, r + 1):
            if p[j] < val:
                smaller += 1

        if smaller == x - l: stdout.write('Yes' + '\n')
        else: stdout.write('No' + '\n')


def __starting_point():
    main()


__starting_point()
