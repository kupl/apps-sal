L, R = map(int, input().split())
if R - L >= 2019:
    print(0)
else:
    list = []
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            list.append(i * j % 2019)
    list = sorted(list)
    print(list[0])
