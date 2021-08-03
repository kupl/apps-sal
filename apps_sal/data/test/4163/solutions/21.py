N = int(input())
D = [[int(x) for x in input().split(" ")] for _ in range(0, N)]

count = 0
flag = False

for (x, y) in D:
    if x == y:
        count += 1
    else:
        count = 0

    if count == 3:
        print("Yes")
        flag = True
        break

if not flag:
    print("No")
