# 解説を確認、このような、最大（最小値）の出し入れが頻繁にあるデータでは、
# 「優先度付きキュー」というデータ構造を用いると容易になるようだ。
# 新規要素の Push & Pop が O(N log N) でできるとのこと。

from heapq import heapify,heappush,heappop

n=int(input())
a=list(map(int,input().split()))

a1=a[0:n]
a_m=a[n:2*n]
a2=[ -x for x in a[2*n:3*n] ] # nega_list

a1_sums=[sum(a1)]
a2_sums=[sum(a2)]
heapify(a1)
heapify(a2)

# 左のシマに真ん中のシマを徐々に追加し、都度最小値を取り出す
for aa in a_m:
  heappush(a1,aa)
  p=heappop(a1)
  a1_sums.append(a1_sums[-1]+aa-p)

# 右のシマは都度最大値を取り出す
a_m.reverse()
for aa in a_m:
  heappush(a2,-aa)
  p=heappop(a2)
  a2_sums.append(a2_sums[-1]-aa-p)

max_val=-float("inf")
for i in range(0,n+1):
  max_val=max(max_val,a1_sums[i]+a2_sums[n-i])

print(max_val)

