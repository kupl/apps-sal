n = int(input())
list1 = [0] * 10
list2 = []
list4 = []
for i in range(0, n, 1):
    x = input()
    m = len(x)
    list2.append(x[0])
    for i in range(0, m, 1):
        list1[ord(x[i]) - 97] += 10**(m - i - 1)
for i in range(0, 10, 1):
    list3 = [list1[i], chr(i + 97)]
    list4.append(list3)
set2 = set(list2)
list4.sort(reverse=True)
list5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
h = 0
for i in range(0, 10, 1):
    if 0 in list5:
        if list4[i][1] not in set2:
            h = h + list4[i][0] * list5[0]
            del list5[0]
        else:
            h = h + list4[i][0] * list5[1]
            del list5[1]
    else:
        h = h + list4[i][0] * list5[0]
        del list5[0]
print(h)
