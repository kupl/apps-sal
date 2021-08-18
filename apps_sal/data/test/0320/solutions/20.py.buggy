n = int(input())
x = 0
y = 0
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
    x += a[-1][0]
    y += a[-1][1]

if x % 2 == 0 and y % 2 == 0:
    print(0)
elif x % 2 != 0 and y % 2 != 0:
    for i in a:
        if i[0] % 2 != i[1] % 2:
            print(1)
            return
    else:
        print(-1)
else:
    print(-1)
