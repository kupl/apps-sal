x, y = list(map(int, input().split()))
if(x < 0 and y < 0):
    print(x + y, 0, 0, x + y)
elif(x < 0):
    print(x - y, 0, 0, -x + y)
elif(y < 0):
    print(0, - x + y, x - y, 0)
else:
    print(0, x + y, x + y, 0)
