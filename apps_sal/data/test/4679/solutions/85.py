s=[0,0,0]
s[0]=list(input())
s[1]=list(input())
s[2]=list(input())
n=0
for i in range(100000):
    if len(s[n])==0:
        break
    tmp=s[n].pop(0)
    if tmp=="a":
        n=0
    elif tmp=="b":
        n=1
    else:
        n=2

if n==0:
    print("A")
elif n==1:
    print("B")
else:
    print("C")
