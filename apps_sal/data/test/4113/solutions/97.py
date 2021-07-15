n=int(input())

ans= "No"

for i in range(n//4+1):
    for j in range(n//7+1):
        if n==4*i+7*j:
            ans = "Yes"
            break
print(ans)
