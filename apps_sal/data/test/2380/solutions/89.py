n,m=map(int,input().split())
A = list(map(int,input().split()))
B=[]
for i in range(m):
    B.append(list(map(int,input().split())))
A.sort()
B.sort(key=lambda B: B[1], reverse=True)

i=j=0
ans = sum(A)
while j<n:
    newv = B[i][1]
    newc = min(B[i][0],n-j)
    if newv>A[j] :
        for k in range(newc):
            if newv<=A[j+k]:
                break
        else:
            k+=1
        ans+=newv*(k)-sum(A[j:j+k])
        i+=1
        j+=k
    else:
        break
    if i>=m :
        break

print(ans)
