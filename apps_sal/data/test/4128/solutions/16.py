t = int(input())
for i in range(t):
    x = int(input())
    if x % 2 == 0:
        print((x - 2) // 2)
    else:
        print((x - 1) // 2)
