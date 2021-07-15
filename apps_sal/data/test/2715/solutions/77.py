k = int(input())

if k==0:
    print(2)
    print("0 0")

elif k ==1:
    print(2)
    print("2 0")

elif k <=50:
    print(k)
    print((str(k)+" ")*(k-1)+str(k))
    
else:
    l = k // 50
    m = k % 50
    print(50)
    print((str(50+l)+" ")*m+(str(49+l-m)+" ")*(49-m)+str(49+l-m))
