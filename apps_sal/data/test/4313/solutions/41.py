N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
diff=[V[i]-C[i] for i in range(N)]
diff.sort(reverse=True)
x=0
for i in range(N):
    if diff[i]<0:
        break
    x+=diff[i]
print(x)

