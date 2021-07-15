n=int(input())
k=list(map(int, input().split()))
m=[0]*n
time=[0]*n
for i in range(n):
    m[i]=list(map(int, input().split()))
    time[i]=k[i]*15
    for j in range(len(m[i])):
        time[i]+=m[i][j]*5
print(min(time))

