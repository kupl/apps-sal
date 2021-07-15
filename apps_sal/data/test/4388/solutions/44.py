n=input()
ans=""
for i in n:
    if i=="1":
        ans+="9"
    elif i=="9":
        ans+="1"
    else:
        ans=i
print(int(ans))
