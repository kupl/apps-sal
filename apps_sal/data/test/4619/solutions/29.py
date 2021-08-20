(w, h, n) = map(int, input().split())
list = [0, w, 0, h]
for i in range(n):
    (x, y, a) = map(int, input().split())
    if a == 1 and list[0] <= x:
        list[0] = x
    elif a == 2 and list[1] >= x:
        list[1] = x
    elif a == 3 and list[2] <= y:
        list[2] = y
    elif a == 4 and list[3] >= y:
        list[3] = y
    else:
        pass
if list[0] > list[1] or list[2] > list[3]:
    print(0)
else:
    print((list[0] - list[1]) * (list[2] - list[3]))
