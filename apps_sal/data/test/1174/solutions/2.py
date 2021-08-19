"""
Created on Wed Sep 16 17:42:18 2020

@author: liang
"""
import heapq
'\n【優先度付きキュー】\n・ヒープ構造の部分順序付き木\n・挿入、削除、最大値（最小値）の取り出し、要素の値の変更\n\u3000⇒\u3000O(log n)\n・ヒープ生成\n\u3000⇒O(n)\n 【使い方】\n  import heapq\n  ●heapq.heapify(list) #最小値\n  ●heapq.heapify(list(map(lambda x:int(x)*(-1),list))) #最大値は値をひっくり返す\n  ●heapq.heappop(a)\n  ●heapq.heappush(a,1)\n'
(N, M) = map(int, input().split())
A = [int(x) * -1 for x in input().split()]
heapq.heapify(A)
for i in range(M):
    Max = heapq.heappop(A) * -1
    Max //= 2
    heapq.heappush(A, Max * -1)
print(-sum(A))
