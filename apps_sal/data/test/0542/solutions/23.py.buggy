sum1 = 0
sum2 = 0
list1 = []
list2 = []
last = 0

n = int(input())

for i in range(n):
    val = int(input())
    if val > 0:
        sum1 += val
        list1.append(val)
        last = 1
    else:
        sum2 += -val
        list2.append(-val)
        last = -1

if sum1 > sum2:
    print("first")
    return
elif sum1 < sum2:
    print("second")
    return

for i in range(min(len(list1), len(list2))):
    if list1[i] > list2[i]:
        print("first")
        return
    elif list1[i] < list2[i]:
        print("second")
        return

if len(list1) > len(list2):
    print("first")
    return
elif len(list1) < len(list2):
    print("second")
    return

if last > 0:
    print("first")
else:
    print("second")
