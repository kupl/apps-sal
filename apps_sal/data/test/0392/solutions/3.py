n=int(input())
s=set()
for i in range(2,int(n**0.5)+1):
    while n%i==0: s|={i}; n//=i
s|={n}
d=1
for x in s: d*=x
print(d)
