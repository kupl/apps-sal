n=int(input())
s=input().strip()
a=s.count('T')
b=s.count('G')
c=s.count('C')
d=s.count('A')
q=max(a,b,c,d)
e=0
if q==a:
    e+=1
if q==b:
    e+=1
if q==c:
    e+=1
if q==d:
    e+=1
print(e**n%1000000007)
