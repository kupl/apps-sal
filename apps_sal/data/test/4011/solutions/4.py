n = int(input())
a = list(input())
fi = list(map(int,input().split()))
flag = 0
for i in range(n):
    if fi[int(a[i])-1] > int(a[i]) and flag != 2:
        flag = 1
        print(fi[int(a[i])-1],end="")
    elif fi[int(a[i])-1] == int(a[i]) and flag == 1:
        print(a[i],end="")
    else:
        if flag == 1:
            flag = 2
        print(a[i],end="")
    

