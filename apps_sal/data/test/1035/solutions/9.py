A,B=map(int,input().split())

def prime_factorization(n):
    arr=[]
    temp=n

    for i in range(2,int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp//=i
            arr.append(i)

    if temp!=1:
        arr.append(temp)
    
    if arr==[]:
        arr.append(n)
    
    return arr

setA=set(prime_factorization(A))
setB=set(prime_factorization(B))
setAB=setA &setB
if setAB=={1}:
    print(1)
else:
    print(len(setAB)+1)
