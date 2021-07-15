from heapq import *

N = int(input())
As = list(map(int, input().split()))
heapify(As)
while len(As) >= 2:
    A1 = heappop(As)
    A2 = heappop(As)
    heappush(As, A1 * A2)
    
if As[0] > 10 ** 18:
    print((-1))
else:
    print((As[0]))

