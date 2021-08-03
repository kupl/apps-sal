import sys

n = int(input())
s = input()

height = [1] * n
matching = [-1] * n

for i, c in enumerate(s):
    if c == ']':
        height[i] = height[matching[i]]
        continue
    balance = 1
    for j in range(i + 1, n):
        if s[j] == '[':
            balance += 1
        elif s[j] == ']':
            balance -= 1
        height[i] = max(height[i], balance)
        if balance == 0:
            matching[i] = j
            matching[j] = i
            break

max_height = max(height)
cur_height, prev_height = max_height, -1
columns = []

m = 2 * max_height + 1


def draw_bar(pos, height):
    while len(columns) <= pos:
        columns.append([' ' for _ in range(m)])
    upper_plus = max_height - height
    lower_plus = m - upper_plus - 1

    columns[pos][upper_plus] = columns[pos][lower_plus] = '+'
    for i in range(upper_plus + 1, lower_plus):
        columns[pos][i] = '|'


def draw_lines(pos, height):
    while len(columns) <= pos:
        columns.append([' ' for _ in range(m)])

    upper_minus = max_height - height
    lower_minus = m - upper_minus - 1

    columns[pos][upper_minus] = columns[pos][lower_minus] = '-'


pos, h = 0, max_height
for i, c in enumerate(s):
    if i > 0:
        if c == ']' and s[i - 1] == '[':
            pos += 3
        if c == '[' and s[i - 1] == '[':
            h -= 1
        elif c == ']' and s[i - 1] == ']':
            h += 1

    draw_bar(pos, h)
    if c == '[':
        draw_lines(pos + 1, h)
    elif c == ']':
        draw_lines(pos - 1, h)

    pos += 1

for i in range(m):
    line = ''.join(column[i] for column in columns).rstrip()
    print(line)
