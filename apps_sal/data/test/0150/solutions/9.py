def prime(x):
    p=int(n**.5)
    p+=2
    for i in range(3,p,2):
        if x%i==0:
            return False
    return True

def func(n):
    if n%2==0:
        if n==2:
            return 1
        return 2

    if n==1 or n==3 or n==5:
        return 1
    
    if prime(n):
        return 1
    if prime(n-2):
        return 2
    return 3

n=int(input())
ans=func(n)
print(ans)

