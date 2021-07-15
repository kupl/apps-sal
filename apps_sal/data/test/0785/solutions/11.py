n,a,b = list(map(int, input().split(' ')))
A = 6*n
if a*b >= 6*n :
    print(a*b)
    print(a,b)
else :
    R = []
    temp = float("INF")
    for i in range(1, int(A**0.5)+2) :
        j = A//i
        if i*j < A : j+=1
        x = max([a,b,i,j])
        y = max(min(a,b) , min(i,j))
        if temp > x*y :
            temp = x*y
            if b>a : x,y = y,x
            R = [x,y, temp]
    print(R[2])
    print(R[0], R[1])
        

