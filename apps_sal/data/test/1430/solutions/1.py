n,k = map(int,input().split())
s = input()
I  = [0]
for i in range(1,n):
    if s[i-1] != s[i]:
        I.append(i)
I.append(n)
r = len(I)-1
X = []
for i in range(r):
    if s[I[i]] == "0":
        X.append(I[min(2*k+i,r)]-I[i])
    else:
        X.append(I[min(2*k+1+i,r)]-I[i])
print(max(X))
