a = int(input().split()[1])
list1 = list(map(int, input().split()))
if a == 1:
    min1 = list1[0]
    for i in list1:
        if min1 > i:
            min1 = i
    print(min1)
elif a >= 3:
    max1 = list1[0]
    for i in list1:
        if max1 < i:
            max1 = i
    print(max1)
elif a == 2:
    min1 = list1[0]
    min2 = list1[-1]
    if min1 > min2:
        print(min1)
    else:
        print(min2)
