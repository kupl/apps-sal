a, b, c = map(str, input().split())
a = int(a)
if (c == "month"):
    if (a < 30):
        print(12)
    elif(a==30):
        print(11)
    else:
        print(7)
else:
    arr = [52, 52, 52, 52, 53, 53, 52]
    print(arr[a-1])
