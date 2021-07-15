q=int(input())
for i in range(q):
    t=int(input())
    arr=[int(x) for x in input().split()]
    arr.sort()
    pos=True
    lengths=[]
    for j in range(2*t):
        if arr[2*j]!=arr[2*j+1]:
            pos=False
            break
        lengths.append(arr[2*j])
    if pos==True:
        area=lengths[0]*lengths[2*t-1]
        for j in range(t-1):
            if lengths[1+j]*lengths[2*t-2-j]!=area:
                pos=False
                break
    if pos==True:
        print("YES")
    else:
        print("NO")
        

