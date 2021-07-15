N=int(input())
A=list(map(int,input().split()))

c = [0] * (N + 1)
Dx = [0] * (N + 1)
for a in A:
    c[a] += 1 #cは、aという数が出た回数を記録
    Dx[c[a]]+=1
    #Dxは、その回数のところに種類を記録。賢い。

Sx=[0]#初項は0
for j in range(1,N+1):
    Sx.append(Sx[j-1]+Dx[j])
#解法2を真似してみる。
for h in range(1,N+1):
    Sx[h]=Sx[h]/h

x=N
k=1
while k<N+1:
    if x<0:
        for _ in range(N-k+1):
            print((0))
        return
    if k<=Sx[x]:
        print(x)
        k+=1
    else:
        x-=1

