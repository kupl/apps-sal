N=str(input())
S=0
for i in range(len(N)):
    S+=int(N[i])

N=int(N)
if N%S==0:
    ans="Yes"
else:
    ans="No"
print(ans)
