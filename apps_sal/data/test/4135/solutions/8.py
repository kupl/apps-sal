n=int(input())
t=input()
for i in range(1,n+1):
    if n%i==0:
        l=t[0:i]
        ost=t[i:]
        l=l[::-1]
        t=l+ost
print(t)
