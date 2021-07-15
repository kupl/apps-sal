n=input()
d={}
flag=0
for i in n:
    d[i]=1
if len(d.keys())%2==1:
    print("IGNORE HIM!")
else :print("CHAT WITH HER!")
