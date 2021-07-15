
from math import floor,sqrt
from collections import Counter
from functools import reduce
def __starting_point():
    a,b,c=list(map(int, input().split()))
    m = int(input())

    mouse = {"USB":[], "PS/2":[]}
    for _ in range(m):
        p,m = input().strip().split()
        mouse[m].append(int(p))

    for m in list(mouse.keys()):
        mouse[m].sort()

    equipped = 0
    cost = 0
    for i in range(a):
        if i < len(mouse["USB"]):
            cost += mouse["USB"][i]
            equipped += 1
        else:
            break
    for j in range(b):
        if j < len(mouse["PS/2"]):
            cost += mouse["PS/2"][j]
            equipped += 1
        else:
            break

    for k in range(c):
        A = ( a < len(mouse["USB"]) )
        B = ( b < len(mouse["PS/2"]))

        if A:
            if B:
                if mouse["USB"][a] < mouse ["PS/2"][b]:
                    price = mouse["USB"][a]
                    a += 1
                else:
                    price = mouse["PS/2"][b]
                    b += 1
            else:
                price = mouse["USB"][a]
                a += 1

            equipped += 1
            cost += price
        else:
            if B:
                price = mouse["PS/2"][b]
                b += 1
                equipped += 1
                cost += price
            else:
                break

    print(str(equipped) + "  " + str(cost))



__starting_point()
