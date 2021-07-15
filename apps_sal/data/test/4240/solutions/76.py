s,t=input(),input()
n=len(s)



ans="No"

for i in range(n):
    s=s[-1]+s[:-1]
    if s==t:
        ans="Yes"
        break


print(ans)
    

