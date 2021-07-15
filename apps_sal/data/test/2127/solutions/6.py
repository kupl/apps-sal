
QTYPE = 0
X = 0
Y = 1
H = 1
W = 2

def main():
    buf = input()
    n = int(buf)
    query = []
    for i in range(n):
        buf = input()
        buflist = buf.split()
        if int(buflist[1]) > int(buflist[2]):
            query.append([buflist[0], int(buflist[1]), int(buflist[2])])
        else:
            query.append([buflist[0], int(buflist[2]), int(buflist[1])])


    bill_size = [query[0][H], query[0][W]]
    for i in range(n):
        if query[i][QTYPE] == '+':
            bill_size = [max(bill_size[X], query[i][H]), max(bill_size[Y], query[i][W])]
        else:
            if bill_size[X] <= query[i][H] and bill_size[Y] <= query[i][W]:
                print("YES")
            else:
                print("NO")

def __starting_point():
    main()

__starting_point()
