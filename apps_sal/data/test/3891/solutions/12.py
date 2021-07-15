import math
n, m = list(map(int, input().split()))

mn_x = 1211111
mx_x = -1211111
mn_y = 1211111
mx_y = -1211111

for i in range(n):
    x = input()
    for j in range(len(x)):
        if x[j] == 'B':
            mn_x = min(mn_x, j +1)
            mx_x = max(mx_x, j + 1)
            mn_y = min(mn_y, i + 1)
            mx_y = max(mx_y, i + 1)
print((mx_y + mn_y) // 2, (mx_x + mn_x) // 2)

