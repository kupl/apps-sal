s=list(input())
t=list(input())
o=0
for (i,j) in zip(s,t):
    if i!=j:
        o+=1
print(o)
