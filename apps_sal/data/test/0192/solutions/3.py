x,y = map(int,input().split())

arr = [y,y,y]
c = 0
t = 0
while True:
    if(arr.count(x)==3):
        break
    if(t==0):
        arr[0] = arr[1]+arr[2]-1
        if(arr[0]>x):
            arr[0] = x
        t = 1
    elif(t==1):
        arr[1] = arr[0]+arr[2]-1
        if(arr[1]>x):
            arr[1] = x
        t = 2
    elif(t==2):
        arr[2] = arr[0]+arr[1]-1
        if(arr[2]>x):
            arr[2] = x
        t = 0
    c += 1
print(c)
