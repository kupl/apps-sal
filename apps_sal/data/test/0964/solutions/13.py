inp = input().split()
a = [int(inp[0]),int(inp[1])]
b = [int(inp[2]),int(inp[3])]
c = [int(inp[4]),int(inp[5])]
a.sort()
a.reverse()
a.append("A")
b.sort()
b.reverse()
b.append("B")
c.sort()
c.reverse()
c.append("C")
first = [a, b ,c]
first.sort()
first.reverse()
second = [a, b, c]
second.sort()
second.reverse()
third = [a, b, c]
#print(first)
#print(second)

def swap(a):
    temp = a[0]
    a[0] = a[1]
    a[1] = temp

def check_first(x):
    #print(x)
    fla = (x[0][0] == x[1][0] + x[2][0])
    #print(x[0][0], "==", x[1][0], "+", x[2][0])
    #print(fla)
    flb = (x[1][1] == x[2][1] == (x[0][0] - x[0][1]))
    #print(x[1][1], "==", x[2][1], "==", x[0][0] - x[0][1])
    #print(flb)
    return fla and flb

def check_second(x):
    if (x[0][0] == x[1][0]) and (x[0][1] + x[1][1] == x[2][0] == x[0][0]):
        return True
    else:
        return False

flag = False
ind = 0
res = -1
s = ""

while (not flag):
    ind = 1
    if check_first(first):
        break
    swap(first[1])
    if check_first(first):
        break
    swap(first[2])
    if check_first(first):
        break
    swap(first[1])
    if check_first(first):
        break
    ind = 2
    if check_second(second):
        break
    swap(second[2])
    if check_second(second):
        break
    if (third[0][0] == third[1][0] == third[2][0]) and (third[0][0] == third[0][1] + third[1][1] + third[2][1]):
        ind = 3
        break
    flag = True

if flag:
    print(-1)
elif ind == 1:
    print(first[0][0])
    for i in range(first[0][1]):
        print(first[0][2] * first[0][0])
    for i in range(first[1][1]):
        print(first[1][2]*first[1][0] + first[2][2] * first[2][0])
elif ind == 2:
    print(second[2][1])
    for i in range(second[0][1]):
        print(second[0][2]*second[0][0] + second[2][2]*second[2][0])
    for i in range(second[1][1]):
        print(second[1][2]*second[1][0] + second[2][2]*second[2][0])

elif ind == 3:
    print(third[0][0])
    for i in range(third[0][1]):
        print(third[0][2]*third[0][0])
    for i in range(third[1][1]):
        print(third[1][2]*third[0][0])
    for i in range(third[2][1]):
        print(third[2][2]*third[0][0])







