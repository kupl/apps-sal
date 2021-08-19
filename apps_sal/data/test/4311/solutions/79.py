s = int(input())
list_a = [s]
for i in range(1000000):
    if list_a[i] % 2 == 0:
        list_a.append(list_a[i] / 2)
    else:
        list_a.append(3 * list_a[i] + 1)
for (index, ai) in enumerate(list_a, 1):
    if ai in list_a[:index - 1]:
        print(index)
        break
