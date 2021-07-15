x1, y1, x2, y2 = [int(i) for i in input().split()]
if x1 != x2:
    if y1 != y2:
        if abs(x1 - x2) != abs(y1 - y2):
            print(-1)
        else:
            print(x1, y2, x2, y1)
    else:
        delta = abs(x2 - x1)
        print(x1, y1 + delta, x2, y1 + delta)
else:
    if y1 != y2:
        delta = abs(y2 - y1)
        print(x1 + delta, y1, x1 + delta, y2)
    else:
        print(-1)
    


            

