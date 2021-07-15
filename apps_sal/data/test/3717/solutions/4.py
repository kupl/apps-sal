n=int(input())
arr=[]
big=10000000000
negbig=-10000000000
for i in range(n):
    x1,x2,y1,y2=[int(j) for j in input().split()]
    arr.append([[x1,x2],[y1,y2]])
prefix_arr=[ [[negbig,negbig],[big,big]] ]
for i in range(1,n):
    first=prefix_arr[-1]
    second=arr[i-1]
    x1,y1=first[0]
    x2,y2=first[1]
    x3,y3=second[0]
    x4,y4=second[1]
    a1=max(x1,x3)
    b1=max(y1,y3)
    a2=min(x2,x4)
    b2=min(y2,y4)
    if ((x1==negbig and x2==negbig and y1==negbig and y2==negbig) or (x3==negbig and x4==negbig and y3==negbig and y4==negbig )):
        prefix_arr.append([ [negbig,negbig],[negbig,negbig] ] )
    else:
        if (a1<=a2 and b1<=b2):
            prefix_arr.append([[a1,b1],[a2,b2]])
        else:
            prefix_arr.append([ [negbig,negbig],[negbig,negbig] ] )
suffix_arr=[]
for i in range(n):
    suffix_arr.append([])
suffix_arr[-1].append([negbig,negbig])
suffix_arr[-1].append([big,big])
for i in range(n-2,-1,-1):
    flag=1
    first=suffix_arr[i+1]
    second=arr[i+1]
    x1,y1=first[0]
    x2,y2=first[1]
    x3,y3=second[0]
    x4,y4=second[1]
    a1=max(x1,x3)
    b1=max(y1,y3)
    a2=min(x2,x4)
    b2=min(y2,y4)
    if ((x1==negbig and x2==negbig and y1==negbig and y2==negbig) or (x3==negbig and x4==negbig and y3==negbig and y4==negbig ) ):
        suffix_arr[i].extend([[negbig,negbig],[negbig,negbig]])
    else:
        if (a1<=a2 and b1<=b2):
            suffix_arr[i].extend([[a1,b1],[a2,b2]])
        else:
            suffix_arr[i].extend([[negbig,negbig],[negbig,negbig]])

for i in range(n):
    first=prefix_arr[i]
    second=suffix_arr[i]
    x1,y1=first[0]
    x2,y2=first[1]
    x3,y3=second[0]
    x4,y4=second[1]
    a1=max(x1,x3)
    b1=max(y1,y3)
    a2=min(x2,x4)
    b2=min(y2,y4)
    if ((x1==negbig and x2==negbig and y1==negbig and y2==negbig) or (x3==negbig and x4==negbig and y3==negbig and y4==negbig)):
        continue
    else:
        if (a1<=a2 and b1<=b2):
            print(a1,b1)
            break






