a=list(map(int, input().split(" ")))
y=list(map(int, input().split(" ")))
circ=[]
for i in range(a[0]):
    fy=a[1]
    for j in circ:
        delta=abs(y[i]-j[0])
        if delta<=2*a[1]:
            fy=max(fy,j[1]+((2*a[1])**2-delta**2)**.5)
    circ.append([y[i],fy])
for i in circ:
    print(i[1], end=" ")
