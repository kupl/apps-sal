n=int(input())
l=n+1
k=int((2*l)**0.5//1)
if l>=k*(k+1)//2:
    print(n-k+1)
else:
    print(n-(k-1)+1)
