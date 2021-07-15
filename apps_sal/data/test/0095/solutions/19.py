from sys import stdin

n = int(stdin.readline().rstrip())
data = list(map(int, stdin.readline().rstrip().split()))

if n == 1:
    print("YES")
    return

up, hor, down = True, True, True

for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        if not up:
            print("NO")
            return
    elif data[i] == data[i - 1]:
        up = False
        if not hor:
            print("NO")
            return
    else:
        up = False
        hor = False
        if not down:
            print("NO")
            return
print("YES")

