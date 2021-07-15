#https://at274.hatenablog.com/entry/2020/06/29/181102
import collections
N=int(input())
A=list(map(int,input().split()))
c=collections.Counter(A)
A=set(A)
MAX_A=10**6
X=[0]*(MAX_A + 1)#0-MAX_Aまでの整数がAの倍数で何回割られるか
for i in A:
  for j in range(i,MAX_A + 1,i):
    X[j]+=1

#割られた回数が1つしかないものはその数自身で割ったのでカウント
#ただし複数ある場合は除外
ans = len([a for a in A if (X[a] == 1) and (c[a] == 1)])
print(ans)
