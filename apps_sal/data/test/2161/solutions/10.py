n = int(input())
names = {}
for i in range(n):
    entry = input().split(' ')
    (name, k, numbers) = (entry[0], int(entry[1]), entry[2:])
    if not names.__contains__(name):
        names[name] = numbers
    else:
        names[name] += numbers
for name in names:
    lst = sorted(names[name], key=len)
    i = 0
    while i < len(lst):
        letter = lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j].find(lst[i], len(lst[j]) - len(lst[i])) >= 0:
                lst.remove(lst[i])
                i -= 1
                break
        i += 1
    names[name] = lst
print(len(names))
for name in names:
    print('%s %d ' % (name, len(names[name])), end='')
    for ent in names[name]:
        print('%s ' % ent, end='')
    print()
