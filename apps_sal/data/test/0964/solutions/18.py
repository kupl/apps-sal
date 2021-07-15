__author__ = 'User'
def f(arr, value, deep, vis):
    nonlocal flag
    if flag == True:
        return
    fl = False
    #print("Num")
    pos = (0, 0)
    for i in range(n):
        for j in range(n):
            #print(i, j, arr[i][j], end = " ")
            if arr[i][j] == 0:
                pos = (i, j)
                fl = True
                break
        if fl == True:
            break
    #print()    
    #print(n, "N")    
    #print(arr, "AAAAAA")
    #print(pos, vis)
    symbol = value[2]
    for y, x in value[:-1]:
        #print(y, x, "YX" + symbol)
        tarr = arr[:]
        y0, x0 = pos[0], pos[1]
        if y0 < n and x0 < n and arr[y0][x0] == 0:
            if x0 + x - 1 < n and y0 + y - 1 < n:
                tr = True
                for i in range(y0, y0 + y):
                    for j in range(x0, x0 + x):
                        if arr[i][j] != 0:
                            tr = False
                            break
                        arr[i][j] = symbol
                    if tr == False:
                        break
                if tr:
                    """print(tr)
                    for i in range(n):
                        print(*tarr[i])
    
                    print()"""                   
                    if deep == 0:
                        print(n)
                        flag = True
                        for i in range(n):
                            print(*arr[i], sep = '')
                        return
                    for k in range(3):
                        if vis[k] == 0:
                            vis[k] = -1
                            #print(tarr, val[k], deep - 1, vis)
                            f(arr, val[k], deep - 1, vis)
                    """
                    for i in range(n):
                        print(*arr[i])  
                    print()
                    """
                tr = True
                for i in range(y0, y0 + y):
                    for j in range(x0, x0 + x):
                        if arr[i][j] == symbol:
                            arr[i][j] = 0
                        else:
                            tr = False
                            break
                    if tr == False:
                        break




x1, y1, x2, y2, x3, y3 = map(int, input().split())
val = [[(x1, y1), (y1, x1), "A"], [(x2, y2) , (y2, x2), "B"], [(x3, y3) , (y3, x3), "C"]]
s = x1 * y1 + x2 * y2 + x3 * y3
flag = True
mx = max(x1, x2, x3, y1, y2, y3)
if round((s) ** (1/2)) == round((s) ** (1/2), 8):
    n = int(s ** 0.5)
    if n < mx:
        flag = False
else:
    flag = False
if flag == True:
    flag = False
    arr = [n * [0] for i in range(n)]
    for i in range(3):
        deep = 3
        vis = [0] * 3
        vis[i] = -1
        #print(n, "N")
        f(arr, val[i], deep - 1, vis)
    if flag == False:
        print(-1)
else:
    print(-1)
