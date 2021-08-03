list = [0]
n = int(input())
for i in range(1, n + 1):
    list.append(1)
    while list[len(list) - 1] == list[len(list) - 2]:
        del list[len(list) - 2]
        list[len(list) - 1] += 1
for i in range(1, len(list)):
    print(list[i], end=' ')
