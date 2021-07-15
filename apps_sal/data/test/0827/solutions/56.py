n=int(input())
s='110'
t=input()
sn=s*((n+2)//3+1)
ret=0
for i in range(3):
    if sn[i:i+n]==t:
        ret += pow(10,10)-(i+n-1)//3
print(ret)
