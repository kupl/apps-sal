import sys


def get_int_list():
    return list(map(int, input().split()))


h, w = tuple(map(int, input().split()))

data = []
for i in range(h):
    data.append(list([[x, False] for x in input()]))

found = False
for i in range(h):
    for j in range(w):
        if not found and data[i][j][0] == "*" and i > 0 and j > 0 and i < h - 1 and j < w - 1:
            if data[i - 1][j][0] == "*" and data[i + 1][j][0] == "*" and \
                    data[i][j - 1][0] == "*" and data[i][j + 1][0] == "*":
                found = True
                data[i][j][1] = True
                row = i - 1
                while row >= 0 and data[row][j][0] == "*":
                    data[row][j][1] = True
                    row -= 1
                row = i + 1
                while row < h and data[row][j][0] == "*":
                    data[row][j][1] = True
                    row += 1
                column = j - 1
                while column >= 0 and data[i][column][0] == "*":
                    data[i][column][1] = True
                    column -= 1
                column = j + 1
                while column < w and data[i][column][0] == "*":
                    data[i][column][1] = True
                    column += 1

for i in range(h):
    for j in range(w):
        if data[i][j][0] == "*" and not data[i][j][1]:
            print("NO")
            return

print("YES" if found else "NO")
