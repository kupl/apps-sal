n = int(input())
x, y = map(int, input().split())
x += (10 ** 9 + 1)
y += (10 ** 9 + 1)
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = input().split()
    arr[i][1] = int(arr[i][1]) + (10 ** 9 + 1)
    arr[i][2] = int(arr[i][2]) + (10 ** 9 + 1)
t1 = -1
t2 = -1
t3 = -1
t4 = -1
t5 = -1
t6 = -1
t7 = -1
t8 = -1

ind1 = ''
ind2 = ''
ind3 = ''
ind4 = ''
ind5 = ''
ind6 = ''
ind7 = ''
ind8 = ''

for i in range(n):
    x1 = arr[i][1]
    y1 = arr[i][2]
    if x1 == x:
        if y > y1:
            if t4 == -1:
                t4 = y - y1
                ind4 = arr[i][0]
            elif (y - y1) < t4:
                t4 = y - y1
                ind4 = arr[i][0]
        else:
            if t2 == -1:
                t2 = y1 - y
                ind2 = arr[i][0]
            elif y1 - y < t2:
                t2 = y1 - y
                ind2 = arr[i][0]

    if y1 == y:
        if x > x1:
            if t1 == -1:
                t1 = x - x1
                ind1 = arr[i][0]
            elif (x - x1) < t1:
                t1 = x - x1
                ind1 = arr[i][0]
        else:
            if t3 == -1:
                t3 = x1 - x
                ind3 = arr[i][0]
            elif x1 - x < t3:
                t3 = x1 - x
                ind3 = arr[i][0]

    if abs(x1 - x) == abs(y1 - y):
        if y1 > y:
            if x1 < x:
                if t5 == -1:
                    t5 = x - x1
                    ind5 = arr[i][0]
                elif(x - x1) < t5:
                    t5 = x - x1
                    ind5 = arr[i][0]
            else:
                if t6 == -1:
                    t6 = x1 - x
                    ind6 = arr[i][0]
                elif(x1 - x) < t6:
                    t6 = x1 - x
                    ind6 = arr[i][0]
        else:
            if x1 < x:
                if t8 == -1:
                    t8 = x - x1
                    ind8 = arr[i][0]
                elif (x - x1) < t8:
                    t8 = x - x1
                    ind8 = arr[i][0]
            else:
                if t7 == -1:
                    t7 = x1 - x
                    ind7 = arr[i][0]
                elif (x1 - x) < t7:
                    t7 = x1 - x
                    ind7 = arr[i][0]
if ind1 == "R" or ind1 == 'Q' or ind2 == "R" or ind2 == 'Q' or ind3 == "R" or ind3 == 'Q' or ind4 == "R" or ind4 == 'Q' or ind5 == 'B' or ind5 == 'Q' or ind6 == 'B' or ind6 == 'Q' or ind7 == 'B' or ind7 == 'Q' or ind8 == 'B' or ind8 == 'Q':
    print("YES")
else:
    print("NO")
