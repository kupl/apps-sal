a = int(input())

x = list(map(int, input().split(' ')))[1:]
y = list(map(int, input().split(' ')))[1:]

num = 0
states = []
while len(x) > 0 and len(y) > 0:
    tx = x[0]
    ty = y[0]
    if tx > ty:
        x = x[1:] + [ty] + [tx]
        y = y[1:]
    else:
        y = y[1:] + [tx] + [ty]
        x = x[1:]
    num += 1

    states.append([x, y])

    if num > 10**5:
        if [x, y] in states:
            print(-1)
            quit()

if x == []:
    print(num, 2)
else:
    print(num, 1)
