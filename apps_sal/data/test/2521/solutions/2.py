import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

# (1).左からN + 1～2N個のデータについて、iがいくつあるかのdictionary
# (2).左から2N個のデータのうち、大きい順にN個のデータの和
# (3).左から2N個のデータのうち、小さい順にN個のデータを、大きい順にheapqに入れたもの
# (4).右からN個のデータの和
# (5).右からN個のデータを、大きい順にheapqに入れたもの

# 上記を用いて、iを2N～N+1までずらし、そのたびに
# A[i]の数を(1)から減らす
# 次の数を(3)から取り出す。その数が(1)に存在していなければ何もしない
# 取り出した数を(2)に足す
# (4)にA[i]を足す
# (5)から一つ取り出し、(4)から引く
# (2) - (4)の最大値を更新

from collections import defaultdict

sortA = sorted(A[:2 * N])
smallA = sortA[:N]
small_dic = defaultdict(int)
for i in range(len(smallA)):
  small_dic[smallA[i]] += 1
largeA = sortA[N:]
large_dic = defaultdict(int)
for i in range(len(largeA)):
  large_dic[largeA[i]] += 1

leftsum = sum(sortA[N:])

import heapq as hq
leftq = list([-x for x in smallA])
hq.heapify(leftq)

rightq = A[2 * N:]
rightsum = sum(rightq)
rightq = list([-x for x in rightq])
hq.heapify(rightq)

ans = leftsum - rightsum

#print("leftsum",leftsum,"rightsum",rightsum,"ans",ans)
for i in range(2 * N - 1, N - 1, -1):
  #print("i",i,"A[i]",A[i])
  if large_dic[A[i]] > 0: # 除外対象である場合
    large_dic[A[i]] -= 1
    leftsum -= A[i]
    while True:
      move = -hq.heappop(leftq)
      if small_dic[move] > 0:
        small_dic[move] -= 1
        break
    leftsum += move
    large_dic[move] += 1
    #print("leftsumから",A[i],"を除外",leftsum)
  else:
    small_dic[A[i]] -= 1
    
  hq.heappush(rightq, -A[i])
  rem = -hq.heappop(rightq)
  rightsum += A[i]
  rightsum -= rem
  
  if ans < leftsum - rightsum:
    ans = leftsum - rightsum
  #print("leftsum",leftsum,"rightsum",rightsum,"ans",ans)
    
print(ans)

