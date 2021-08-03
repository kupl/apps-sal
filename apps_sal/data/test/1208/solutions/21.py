n = int(input())
minCapacity = 0
capacity = 0
readersIn = []
for i in range(0, n):
    rec = input().split()
    if (rec[0] == '+'):
        capacity += 1
        readersIn.append(rec[1])
    elif (rec[0] == '-'):
        if(readersIn.__contains__(rec[1])):
            readersIn.remove(rec[1])
            capacity -= 1
        else:
            minCapacity += 1
    if (capacity > minCapacity):
        minCapacity = capacity

print((str(minCapacity)))
