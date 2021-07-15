l = list(map(int, input().split()))
x_l, y_l = l[0:2], l[2:4]

max_result = float('-inf')

for x in x_l:
    for y in y_l:
        result = x * y
        if max_result < result:
            max_result = result
print(max_result)
