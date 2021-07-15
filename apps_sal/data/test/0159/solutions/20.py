import fractions
import sys
n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(1,n):
    ans.append(l[i-1])
    if fractions.gcd(l[i],l[i-1])>1:
        ans.append("1")
ans.append(l[n-1])
print(len(ans)-n)
for i in ans:
    sys.stdout.write(str(i)+" ")
