n = int(input())
d = 1
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        print(x // 2)
    else:
        if d == 1:
            print(int(x / 2 + 0.5))
            d = 2
        else:
            print(int(x / 2 - 0.5))
            d = 1
