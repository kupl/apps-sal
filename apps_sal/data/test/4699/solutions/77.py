n, k = map(int, input().split())
d = list(input().split())
num = [str(i) for i in range(10)]
for i in range(k):
    num.remove(d[i])
    
import itertools, heapq
ans = []
heapq.heapify(ans)
for i in itertools.product(num, repeat=len(str(n))):
    s = int(''.join(i))
    if s >= n:
        heapq.heappush(ans, s)
        
if len(ans) == 0:
    for i in itertools.product(num, repeat=len(str(n)) + 1):
        s = int(''.join(i))
        if s >= n:
            heapq.heappush(ans, s)
    print(heapq.heappop(ans))
    
else:
    print(heapq.heappop(ans))
