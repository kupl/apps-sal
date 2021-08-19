"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""


def main():
    n = int(input())
    t1 = [int(_) for _ in input().split()]
    t1 = sorted(t1)
    m = int(input())
    t2 = [int(_) for _ in input().split()]
    t2 = sorted(t2)
    a = x = 3 * n
    b = y = 3 * m
    advantage = a - b
    i = 0
    j = 0
    while i < n or j < m:
        if i < n and j < m:
            if t1[i] < t2[j]:
                x -= 1
                i += 1
            elif t2[j] < t1[i]:
                y -= 1
                j += 1
            else:
                x -= 1
                y -= 1
                i += 1
                j += 1
        elif i < n:
            x -= 1
            i += 1
        else:
            y -= 1
            j += 1
        if x - y > advantage:
            a = x
            b = y
            advantage = a - b
    print('%d:%d' % (a, b))


def __starting_point():
    main()


__starting_point()
