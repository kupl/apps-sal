N = int(input())
A = list(map(int, input().split()))
color = [0] * 9
for a in A:
    if a <= 399:
        color[0] = 1
    elif a <= 799:
        color[1] = 1
    elif a <= 1199:
        color[2] = 1
    elif a <= 1599:
        color[3] = 1
    elif a <= 1999:
        color[4] = 1
    elif a <= 2399:
        color[5] = 1
    elif a <= 2799:
        color[6] = 1
    elif a <= 3199:
        color[7] = 1
    else:
        color[8] += 1
max_num = sum(color)
min_num = max(1, sum(color[:-1]))
print(min_num, max_num)
