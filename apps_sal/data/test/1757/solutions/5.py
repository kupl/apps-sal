ar=[1]+[0]*(2000)
f1,f2=1,1
while f1 <= len(ar):
    ar[f1]=1
    f1,f2=f1+f2,f1
n=int(input())
s=""
for x in range(n):
    s+="O" if ar[x+1] else "o"
print(s)
