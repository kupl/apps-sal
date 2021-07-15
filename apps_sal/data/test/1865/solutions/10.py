n = int(input())
a = [int(m) for m in input().split()]
counter = 0
exit_list = []
i = 0
while i < n:
    sublist = a[i:]
    minimum = sublist.index(min(sublist)) + i
    if i != minimum:
        exit_list.append((i, minimum))
        c = a[minimum]
        a[minimum] = a[i]
        a[i] = c
        counter += 1
    i += 1
print(counter)
for x in exit_list:
    print(x[0], x[1])
