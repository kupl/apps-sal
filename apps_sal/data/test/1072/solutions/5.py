def sortedx(lst):
    copy = lst[:]
    copy.sort()
    if copy == lst:
        return True
    return False

a, b = list(map(int, input().split(' ')))
words = [input() for i in range(a)]
each = ['' for i in range(a)]

for j in range(b):
    if sortedx([each[i] + words[i][j] for i in range(a)]):
        for ix in range(a):
            each[ix] = each[ix] + words[ix][j]
            

print(b - len(each[0]))

