import sys


top = [-1] * 8
top_let = [''] * 8
down = [-1] * 8
down_let = [''] * 8

for i in range(8):
    s = input().strip()
    j = 0
    while j < 8:
        if s[j] == 'W' or s[j] == 'B':
            if top[j] == -1:
                top[j] = i
                top_let[j] = s[j]

            down[j] = i
            down_let[j] = s[j]

        j += 1

min_w = 10
max_b = -1
for i in range(8):
    if top_let[i] == 'W' and min_w > top[i]:
        min_w = top[i]

    if down_let[i] == 'B' and max_b < down[i]:
        max_b = down[i]

if min_w > 8 - max_b - 1:
    print('B')
else:
    print('A')
