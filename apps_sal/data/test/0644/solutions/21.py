from collections import defaultdict as dd
import math
import sys


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


q = nn()


x = 0
forstack = []
forproduct = 1
badfors = 0
willoverflow = False
bad = 0
for _ in range(q):

    l = input().split(' ')

    if len(l) == 2:
        if willoverflow:
            forstack.append(int(l[1]))
            badfors += 1
        else:
            forstack.append(int(l[1]))
            forproduct *= int(l[1])
            if x + forproduct > 2**32 - 1:
                willoverflow = True
                badfors = 1

    elif l[0] == 'add':
        if willoverflow:
            print("OVERFLOW!!!")
            bad = 1
            break
        x += forproduct
        if x > 2**32 - 1:
            print("OVERFLOW!!!")
            bad = 1
            break

    elif l[0] == 'end':
        p = forstack.pop()
        if willoverflow:
            badfors -= 1

            if badfors == 0:
                forproduct //= p
                willoverflow = False
        else:
            forproduct //= p

if bad == 0:
    print(x)
