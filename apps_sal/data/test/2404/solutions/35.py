n=int(input())
s=''
for i in range(int(n**0.5),0,-1):
    if n%i==0:
        s=s+str(i)+str(n//i)
        break
print(s)

