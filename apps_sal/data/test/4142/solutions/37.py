s=list(input())
kisu=s[::2]
gusu=s[1::2]
flag=0
for e in kisu:
    if e =="R" or e=="U" or e=="D":
        flag+=1
for e in gusu:
    if e =="L" or e=="U" or e=="D":
        flag+=1
if flag==len(s):
    print("Yes")
else:
    print("No")
