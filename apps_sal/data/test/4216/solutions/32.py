from math import sqrt

n = int(input())
ans = float("INF")
for i in range(1,int(sqrt(n))+1):
    if n%i == 0:
        j = n//i
        ans = min(ans,max(len(str(i)),len(str(j))))
print(ans)

