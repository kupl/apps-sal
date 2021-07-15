import heapq as hq
x,y,z,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ab = []
for a in A:
    for b in B:
        hq.heappush(ab, -a-b)
abc = []
cnt = 0
while cnt < k and ab:
    cnt += 1
    a = hq.heappop(ab)
    for b in C:
        hq.heappush(abc, a-b)
cnt = 0
while cnt < k:
    print(-hq.heappop(abc))
    cnt += 1
