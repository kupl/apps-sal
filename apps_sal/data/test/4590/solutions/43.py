def getmax(x,y):
    if x>y:
        return x
    else:
        return y
N,M,K = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a,b = [0],[0]
for i in range(N):   #a[i]にはAの本をi冊読んだ時の時間がそれぞれ保存されている．
    a.append(a[i]+A[i])  #計算量を減らすため，a[i]（1冊前までにかかる時間）を用いる
for i in range(M):
    b.append(b[i]+B[i])

ans,j = 0,M
for i in range(N+1):
    if a[i]>K:
        break
    while b[j] > K-a[i]:    #Bの本を読んだ場合の処理はここで実行される．
        j -=1
    ans = max(ans, i+j)
print(ans)

