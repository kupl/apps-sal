(len_x, len_y) = list(map(int, input().split()))
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
ans = 0
i = 0
j = 0
add_x = 0
add_y = 0
while i < len_x and j < len_y:
    if add_x == add_y:
        ans += 1
        add_x = x[i]
        add_y = y[j]
        i += 1
        j += 1
    elif add_x < add_y:
        add_x += x[i]
        i += 1
    else:
        add_y += y[j]
        j += 1
print(ans)
