import sys
input=sys.stdin.readline #文字列入力はするな！！
import heapq
n,m=list(map(int,input().split()))
a=[]
for i in input().split():
    heapq.heappush(a,-int(i))
for i in range(m):
    p=-heapq.heappop(a)
    p=p//2
    heapq.heappush(a,-p)
print((-sum(a)))


