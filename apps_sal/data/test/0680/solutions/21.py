(x_A, y_A) = list(map(int, input().split()))
(x_B, y_B) = list(map(int, input().split()))
(x_C, y_C) = list(map(int, input().split()))
'\nWAY_X = max(x_A, x_B, x_C) - min(x_A, x_B, x_C) + 1\nWAY_y = max(y_A, y_B, y_C) - min(y_A, y_B, y_C) + 1\nif x_A == x_B == x_C or y_A == y_B == y_C:\n    cross = 0\nelif x_A == x_B or x_A == x_C or x_B == x_C:\n    cross = 1\nelif y_A == x_B or y_A == y_C or y_B == y_C:\n    cross = 1\nelse:\n    cross = 2\nprint(WAY_X, WAY_y, cross)\n'
if x_A >= x_B >= x_C:
    (x_A, x_B, x_C) = (x_C, x_B, x_A)
    (y_A, y_B, y_C) = (y_C, y_B, y_A)
elif x_A >= x_C >= x_B:
    (x_A, x_B, x_C) = (x_B, x_C, x_A)
    (y_A, y_B, y_C) = (y_B, y_C, y_A)
elif x_B >= x_A >= x_C:
    (x_A, x_B, x_C) = (x_C, x_A, x_B)
    (y_A, y_B, y_C) = (y_C, y_A, y_B)
elif x_B >= x_C >= x_A:
    (x_A, x_B, x_C) = (x_A, x_C, x_B)
    (y_A, y_B, y_C) = (y_A, y_C, y_B)
elif x_C >= x_A >= x_B:
    (x_A, x_B, x_C) = (x_B, x_A, x_C)
    (y_A, y_B, y_C) = (y_B, y_A, y_C)
(pos_x, pos_y) = (x_A, min(y_A, y_B, y_C))
count = 0
ans = ''
while pos_x < x_B:
    ans += str(pos_x) + ' ' + str(y_A) + '\n'
    pos_x += 1
    count += 1
while pos_y <= max(y_C, y_A, y_B):
    ans += str(x_B) + ' ' + str(pos_y) + '\n'
    pos_y += 1
    count += 1
while pos_x < x_C:
    pos_x += 1
    ans += str(pos_x) + ' ' + str(y_C) + '\n'
    count += 1
print(count)
print(ans[:-1])
