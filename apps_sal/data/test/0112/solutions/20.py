import sys
n = int(input())
max = 0
if n == 1:
    a = [int(x) for x in input().split()]
    for i in range(1, 10):
        if i not in a:
            print(max)
            return
        max += 1
elif n == 2:
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for i in range(1, 10):
        if (i not in a) and (i not in b):
            print(max)
            return
        max += 1
    for i in range(10, 100):
        a1 = int(str(i)[0])
        a2 = int(str(i)[1])
        if ((a1 in a) and (a2 in b)) or ((a1 in b) and (a2 in a)):
            max += 1
        else:
            print(max)
            return
elif n == 3:
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    for i in range(1, 10):
        if (i not in a) and (i not in b) and (i not in c):
            print(max)
            return
        max += 1
    for i in range(10, 100):
        a1 = int(str(i)[0])
        a2 = int(str(i)[1])
        if ((a1 in a) and (a2 in b)) or ((a1 in b) and (a2 in a)) or ((a1 in a) and (a2 in c)) or ((a1 in c) and (a2 in a)) or (a1 in b) and (a2 in c) or (a1 in c) and (a2 in b):
            max += 1
        else:
            print(max)
            return
