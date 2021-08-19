t = int(input())
for i in range(t):
    x = int(input())
    if x <= 7:
        print(1)
    elif x % 2:
        x -= 3
        print(1 + x // 2)
    else:
        print(x // 2)
