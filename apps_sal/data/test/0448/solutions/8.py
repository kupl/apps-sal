n, m = tuple(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
result = -2
finished = False

while finished == False:
    finished = True
    last_child = -1
    for index, el in enumerate(a):
        if el <= 0:
            continue
        if el > m:
            finished = False
        else:
            last_child = index + 1
        a[index] = el - m

print(last_child)
