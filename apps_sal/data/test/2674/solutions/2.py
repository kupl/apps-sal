# cook your dish here
t=input()
s=str(t)
ans='Inclusive'
p=0
for c in s:
    p=p ^ int(c)
if p==0:
    ans='Exclusive'
print(ans)
