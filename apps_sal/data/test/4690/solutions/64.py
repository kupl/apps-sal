S_list = iter(list(map(int, input().split())))
area = list()
for x, y in zip(S_list, S_list):
    area.append(x * y)
print(max(area))
