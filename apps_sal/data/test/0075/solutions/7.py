x, y = list(map(int, input().split(' ')))
map_x, map_y = {}, {}
max_r, max_rv = 0, 0
max_c, max_cv = 0, 0
str_l = []

for _ in range(x):
    str = input()
    str_l.append(str)
    for i in range(len(str)):
        if str[i] == '*':
            if i not in map_y:
                map_y[i] = {}
            map_y[i][_] = None

# transpose string arrays
str_t = list(zip(*str_l))

# find column contains max number of walls
for _ in range(y):
    walls = str_t[_].count('*')
    if walls > max_cv:
        max_c = _
        max_cv = walls

# find row contains max number of walls
for _ in range(x):

    walls = str_l[_].count('*')

    if walls > max_rv:
        max_r = _
        max_rv = walls

    # if number same, then do a smart row choice
    elif walls == max_rv:
        if str_l[_][max_c] == '.':
            max_r = _
            max_rv = walls


def check(r, c):

    sum = 1 if c in map_y else 0

    # remove from column
    for yy in range(y):
        if yy in map_y and yy != c:
            if len(map_y[yy]) == 1 and r in map_y[yy]:
                sum += 1

    return len(map_y) == sum

for c in range(y):
    if check(max_r, c) is True:
        print("YES")
        print(max_r+1, c+1)
        return

print("NO")

