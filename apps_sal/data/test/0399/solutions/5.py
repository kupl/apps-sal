x, y = [int(i) for i in input().split()]


a = y
b = a - 1

if y == 1:
    if x > 0:
        print("No")
    else:
        print("Yes")
elif x < b or y < 1 or (x-b)%2 == 1:
    print("No")
else:
    print("Yes")


