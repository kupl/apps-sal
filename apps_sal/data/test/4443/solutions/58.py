l=list("abcdefghijklmnopqrstuvwxyz")
ans=input()
for i in range(len(l)):
    if l[i]==ans:
        print(l[i+1])
        break
