s = int(input())
li = []
li.append(s)

for i in range(1, 1000000000):
    if li[i - 1] % 2 == 0:
        li.append(li[i - 1] // 2)
    else:
        li.append(li[i - 1] * 3 + 1)

    for j in range(len(li) - 1):
        if li[j] == li[i]:
            print((i + 1))
            return
