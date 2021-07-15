n,m = map(int,input().split())
A=[]
B=[]
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
cnt=0
flag = False
for i in range(n-m+1):
    for j in range(n-m+1):
        ans = 'Yes'
        for k in range(m):
            for l in range(m):
                if A[i+k][j+l]!=B[k][l]:
                    ans = 'No'
        else:
            if ans == 'Yes':
                print(ans)
                return
print(ans)
