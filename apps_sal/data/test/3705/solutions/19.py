n=int(input())
c=0
s=input()
for i in s:
    if i=='8':c+=1
print(min(n//11,c))
