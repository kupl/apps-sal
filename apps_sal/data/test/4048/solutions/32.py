n=int(input())

for i in range(int(n**0.5),0,-1):
    if n%i==0:
        a=i
        b=n//i
        break
print((a-1+b-1))

