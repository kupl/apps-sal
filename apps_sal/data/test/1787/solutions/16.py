check=input()
ans=0
back=0
for i in range (len(check)-1,-1,-1):
    if check[i:i+1]=='a':
        ans+=((1+back)%(10**9+7))
    elif check[i:i+1]=='b':
        back=ans
print(ans%(10**9+7))
