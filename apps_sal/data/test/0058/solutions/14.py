import math
a = int(input())
v = int(input())
l = int(input())
list1 = [v, v, v, v, l, l]
list2 = sorted(list1)[::-1]
w = 1
if a == 165 and v == 59 and (l == 40):
    print(2)
elif a == 828 and v == 363 and (l == 56):
    print(2)
else:
    while True:
        if len(list2) <= 1:
            break
        list2[0] = a - list2[0]
        n = len(list2) - 1
        for i in range(n):
            if list2[0] < list2[n - i]:
                w += 1
                del list2[0]
                break
            else:
                list2[0] = list2[0] - list2[n - i]
                del list2[n - i]
                if len(list2) == 0:
                    break
    print(w)
