lines = int(input())
if lines == 1:
    print(1)
    return
grid = []
number_with_zero = set()
impossible = False
no_zero = -1

for x in range(lines):
    num = list(map(int, input().split()))
    grid.append(num)

for line in grid:
    have_zero = False
    s = 0
    for n in line:
        if n == 0:
            have_zero = True
        else:
            s += n
    if have_zero:
        number_with_zero.add(s)
    elif no_zero == -1:
        no_zero = s
    elif no_zero != s:
        impossible = True

# print(impossible, 1)
for x in range(lines):
    have_zero = False
    s = 0
    for y in range(lines):
        n = grid[y][x]
        if n == 0:
            have_zero = True
        else:
            s += n
    if have_zero:
        number_with_zero.add(s)
    elif no_zero == -1:
        no_zero = s
    elif no_zero != s:
        impossible = True
# print(impossible, 2)

s = 0
have_zero = False
for x in range(lines):
    n = grid[x][x]
    if n == 0:
        have_zero = True
    else:
        s += n

# print(s, no_zero)
if have_zero:
    number_with_zero.add(s)
elif no_zero == -1:
    no_zero = s
elif no_zero != s:
    impossible = True
# print(impossible, 3)

s = 0
have_zero = False
for x in range(lines):
    n = grid[x][lines - 1 - x]
    if n == 0:
        have_zero = True
    else:
        s += n

if have_zero:
    # print("COME")
    number_with_zero.add(s)
elif no_zero == -1:
    no_zero = s
elif no_zero != s:
    impossible = True
# print(impossible, 4)

if impossible:
    print(-1)
else:
    if len(number_with_zero) == 1:
        num = list(number_with_zero)[0]
        # print(num)
        if (no_zero - num <= 0):
            print(-1)
        else:
            print(no_zero - num)
    else:
        print(-1)
