#<D>
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
X = sorted([list(map(int, input().split())) for n in range(N)], key = lambda x: x[0])
#print(X)
hq = []
ans, j = 0, 0

for i in range(1, M + 1): #M - i日後にするバイトを決める
    while (j < N) and (X[j][0] <= i):
        heappush(hq, -X[j][1]) # 候補の追加
        j += 1
    if len(hq):
        ans += - heappop(hq) #候補があるなら候補から最大値を取り出す
print(ans)

