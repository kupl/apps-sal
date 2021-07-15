n=int(input())
s=input()
W=0 ; E=s[1:].count("E")
ans=float("inf")
for i in range(n):
    ans=min(ans, W+E)
    if i==n-1:print(ans);return
    if s[i]=="W":
        W+=1
    if s[i+1]=="E":
        E-=1
