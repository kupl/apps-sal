inp_arr = [tuple(map(int, input().split())) for i in range(8)]
x_set = set()
y_set = set()
for x, y in inp_arr:
    x_set.add(x)
    y_set.add(y)

if len(x_set) == len(y_set) == 3:
    ugly = False
    x_sort, y_sort = sorted(x_set), sorted(y_set)
    for x in x_sort:
        for y in y_sort:
            if (x, y) != (x_sort[1], y_sort[1]) and (x, y) not in inp_arr:
                ugly = True
else:
    ugly = True
print("ugly" if ugly else "respectable")
