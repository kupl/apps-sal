import copy
n = int(input())
an = [int(input()) for i in range(n)]
bn = copy.copy(an)
top = max(an)
an.remove(top)
top2 = max(an)


for x in bn:
    if x == top:
        print(top2)
    else:
        print(top)
