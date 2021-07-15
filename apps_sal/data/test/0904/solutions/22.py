def find(s):
    c=0
    for i in range(len(s)):
        T=s[i]
        if ord(T)<=90 and ord(T)>=65:
            c+=1
    return c
input()
s=list(input().strip().split(' '))
MAX=0
for x in s:
    T=find(x)
    if T>MAX:
        MAX=T
print(MAX)        

