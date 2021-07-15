n=int(input())
series=list(map(int,input().split()))
smotrel=[False]*100000
for i in series:
    smotrel[i-1]=True
for i in range(n):
    if not smotrel[i]:
        break
print(i+1)

