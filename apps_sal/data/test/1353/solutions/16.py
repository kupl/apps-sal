n,m,a,b = list(map(int,list(input().split())))
k = 0
cost = b / m
if(cost <= a):
    k += int(n / m)*b
    if(n%m*a < b):
        k += (n%m)*a
    else:
        k+=b
else:
    k = a*n
print(k)
    

