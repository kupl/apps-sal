s = int(input())

count = 1
n = s
check = 0
list = [s]


for i in range(30000):
    if n % 2 == 0:
        n = n / 2
        list.append(n)
    else:
        n = n * 3 + 1
        list.append(n)

    count = count + 1
    list.sort()
    for j in range(len(list) - 1):
        if list[j] == list[j + 1]:
            check = 1
            break

    if check == 1:
        break


print(count)
