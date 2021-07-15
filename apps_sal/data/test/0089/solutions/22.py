n = int(input())
k = (n//2)*(n//2+1)
print(k if n%2==0 else k+(n+1)//2)

