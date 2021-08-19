import math
table = []
a = 1
for i in range(5):
    x = list(map(int, input().split()))
    if a in x:
        row_in = i + 1
        col_in = x.index(a) + 1
    table.append(x)
#print(row_in, col_in)
steps = math.fabs((3 - (row_in))) + math.fabs((3 - (col_in)))
print(int(steps))
