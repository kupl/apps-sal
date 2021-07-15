n=int(input())
for i in range(0,(n-1)//2):
    j=2*i+1
    k=(n-j)//2
    print('*'*k+'D'*j+'*'*k)
print("D"*n)
for i in range(0,(n-1)//2):
    ii=(n-1)//2-i-1
    j=2*ii+1
    k=(n-j)//2
    print('*'*k+'D'*j+'*'*k)
