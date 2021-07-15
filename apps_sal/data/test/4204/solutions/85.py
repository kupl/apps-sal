s=input()
k=int(input())
c=0
for i in s:
    if i=='1':
        c+=1  
    else:
        break
print(s[c] if k>c else "1")
