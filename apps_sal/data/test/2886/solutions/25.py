s=input()
n=len(s)
accum=[[0]*(n+1) for _ in range(26)]
for i in range(n):
    accum[ord(s[i])-ord("a")][i+1]+=1
for i in range(n):
    for j in range(26):
        accum[j][i+1]+=accum[j][i]
for i in range(n-1):
    for j in range(26):
        if accum[j][i+2]-accum[j][i]==2:
            print(i+1,i+2)
            return
for i in range(n-2):
    for j in range(26):
        if accum[j][i+3]-accum[j][i]==2:
            print(i+1,i+3)
            return
print(-1,-1)
