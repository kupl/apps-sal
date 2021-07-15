n,k = map(int,input().split())
s = input()
L = [0]*len(s)
for i in range(len(s)-1):
    if s[i] == "A" and s[i+1] =="C":
        L[i+1] = 1
L = [0]+L
for i in range(1,len(s)+1):
    L[i]+=L[i-1]
#print(L)
for i in range(k):
    a,b = map(int,input().split())
    print(L[b]-L[a])
