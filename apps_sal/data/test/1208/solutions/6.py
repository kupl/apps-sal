N = int(input())
number = 0
maxnum = 0
visitors = dict()
for n in range(N):
    (inout, ID) = input().split()
    if inout == '+':
        visitors[ID] = 1
        number += 1
    else:
        if ID not in visitors:
            maxnum += 1
        else:
            number -= 1
        visitors[ID] = 0
    if number > maxnum:
        maxnum = number
print(maxnum)
