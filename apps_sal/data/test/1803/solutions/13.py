birds = int(input())
total = list(map(int, input().split()))
shots = int(input())
if birds == 1 and shots == 1:
    print(0)
    return
if birds == 1 and shots == 0:
    print(total[0])
    return
for i in range(shots):
    x, y = tuple(map(int, input().split()))
    x = x - 1
    if x == 0:
        total[1] += total[0] - y
    elif x == len(total) - 1:
        total[x - 1] += y - 1
    else:
        total[x + 1] += total[x] - y
        total[x - 1] += y - 1
    total[x] = 0
for i in total:
    print(i)
