x = int(input())
x = x % 360
if (x <= 45 or x >= 315):
    print(0)
elif (x >= 45 and x <= 135):
    print(1)
elif (x >= 135 and x <= 225):
    print(2)
else:
    print(3)

