"""Ввод размера матрицы"""
nm = [int(s) for s in input().split()]

"""Ввод массива"""
a = []
for i in range(nm[0]):
    a.append([int(j) for j in input().split()])

rez=[]

def stroka():
    nonlocal rez
    rez_row=[]
    rez_r=0
    for i in range(nm[0]):
        min_row=501
        for j in range(nm[1]):
            if a[i][j]< min_row:
                min_row=a[i][j]
        rez_r+=min_row

        if min_row != 0:
            for c in range(min_row):
                rez.append('row ' + str(i+1))

        for j in range(nm[1]):
            if a[i][j]>0:
                a[i][j]-= min_row

def grafa():
    nonlocal rez
    rez_c=0
    for j in range(nm[1]):
            min_col=501
            for i in range(nm[0]):
                if a[i][j]< min_col:
                    min_col=a[i][j]
            rez_c+=min_col

            if min_col !=0:
                for c in range(min_col):
                    rez.append('col '+ str(j+1))
            for i in range(nm[0]):
                if a[i][j]>0:
                    a[i][j] -=min_col


if nm[0]<nm[1]:
    stroka()
    grafa()
else:
    grafa()
    stroka()

maxEl = max(max(a))

if maxEl == 0:
    print(len(rez))
    for el in rez:
        print(el)
else:
    print(-1)

