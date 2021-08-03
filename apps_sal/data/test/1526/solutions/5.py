
lst = list(map(int, input().split()))
# print(lst)
lst.sort()
count = 0
while len(set(lst)) != 1:
    for i in range(len(lst) - 2):
        if lst[i] <= lst[i + 1] - 2:
            lst[i] += 2
        elif lst[i] <= lst[i + 2] and lst[i + 1] <= lst[i - 1]:
            lst[i] += 1
            lst[i + 1] += 1
    count += 1
    lst.sort()
    # print(lst)
print(count)
