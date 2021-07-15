pl = 0
etpl = 0
max_x = 0
min_x = 40000
max_y = 0
min_y = 40000
n = int(input())
for i in range(0,n,1):
    crd = input().split()
    if(int(crd[0]) >= int(crd[2])):
        st1 = int(crd[0]) - int(crd[2])
    else:
        st1 = int(crd[2]) - int(crd[0])
    if(int(crd[1]) >= int(crd[3])):
        st2 = int(crd[1]) - int(crd[3])
    else:
        st2 = int(crd[3]) - int(crd[1])
    if(int(crd[0]) < min_x):
        min_x = int(crd[0])
    if(int(crd[1]) < min_y):
        min_y = int(crd[1])
    if(int(crd[2]) > max_x):
        max_x = int(crd[2])
    if(int(crd[3]) > max_y):
        max_y = int(crd[3])
    pl += st1*st2
    etpl = (max_y-min_y)*(max_x-min_x)
if max_y-min_y == max_x-min_x and etpl == pl:
    print("YES")
else:
    print("NO")
