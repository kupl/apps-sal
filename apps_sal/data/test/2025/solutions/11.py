easy = [1, 2, 3, 5, 7, 11]

def cheker(i):
    if i in easy:
        print(-1)
    elif i % 2 == 0 and i % 4 != 0:
        if i == 6:
            print(1)
        else:
            print(1 + (i - 6)//4)
    elif i % 4 == 0:
        print(i//4)
    elif (i - 1) % 4 == 0:
        if i == 9:
            print(1)
        else:
            print(1 + (i - 9) // 4)
    elif (i + 1) % 4 == 0:
        print((i-9-6)//4 + 2)




l = int(input())
for i in range(l):
    now = int(input())
    cheker(now)

