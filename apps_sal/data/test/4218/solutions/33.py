n = int(input())
if n==1:
    print(1)
else:
    if n%2==0:
        kisu=n//2
    else:
        kisu=n//2+1
    print(kisu/n)
