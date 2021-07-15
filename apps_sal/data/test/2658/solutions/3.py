N, K = map(int,input().split())
A = list(map(int,input().split()))

check = [0] * (N+1) #対象の町を訪問するのが初めてか
li = [] #町の移動順
i, j = 1, 1 #現在の町の番号と移動回数

while True:
  k = A[i-1] #移動先の町の番号
  if check[k] == 1:
    #前に訪問したことがある場合
    n = li.index(k)+1 #ループに入った時点での移動回数
    break
  check[k] = 1
  li.append(k)
  i = k
  j += 1

if K < n: print(li[K-1])
else: print(li[(K-n) % (j-n) + n - 1])
