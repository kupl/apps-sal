n = input()
arr = [int(x) for x in input().split()]
arr.sort()

x1, x2 = arr[0], arr[1]
y1, y2 = arr[-1], arr[-2]

if (y2 - x1) > (y1 - x2):
    print(y1 - x2)
else:
    print(y2 - x1)

