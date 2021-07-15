a = [int(s) for s in input().split()]
b = [int(s) for s in input().split()]
if (a[1] == 1):
    minimum = b[0]
    for i in range(a[0]):
        if (minimum > b[i]):
            minimum = b[i]
    print(minimum)
elif (a[1] >= 3):
    maximum = b[0]
    for i in range(a[0]):
        if (maximum < b[i]):
            maximum = b[i]
    print(maximum)
elif (a[1] == 2 and a[0] == 2):
    print(max(b[0], b[1]))
else:
    print(max(b[0], b[a[0] - 1]))
