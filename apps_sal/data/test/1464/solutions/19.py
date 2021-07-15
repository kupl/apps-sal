from string import ascii_lowercase
dict={}
f=0
n=int(input())
k=0
s=""
l=[]
l1=[]
m=0
for i in range(0,n):
    s=input()
    l1.append(s)
l1 = [i.strip() for i in l1]
str="a"
while f==0:
    m=0
    for i in range(0,n):
        s=''.join(l1[i])
        if str in s:
            m=m+1
    if m!=0:
            if str[k]=="z":
                j=k
                while(str[j]=='z' and j>=0):
                    str=str.replace(str[k],"a")
                    j=j-1
                if(j==-1):
                    str=str+"a"
                    k=k+1
                else:
                    str=str[:j]+chr(ord(str[j])+1)+str[j+1:]
            else:
                str=str[:k]+chr(ord(str[k])+1)
    else:
        f=1
        break;
print(str)
