import heapq

x,y,a,b,c = list(map(int,input().split()))

p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

ans = 0
red_cnt = 0
green_cnt = 0
cnt = 0

heap = []
for i in range(len(p)):
    heapq.heappush(heap,(-p[i],0))
for i in range(len(q)):
    heapq.heappush(heap,(-q[i],1))
for i in range(len(r)):
    heapq.heappush(heap,(-r[i],2))

while len(heap):
    _x,_y = heapq.heappop(heap)
    if _y == 0 and red_cnt < x:
        red_cnt += 1
        ans += _x
        cnt += 1
    elif _y == 1 and green_cnt < y:
        green_cnt += 1
        ans += _x
        cnt += 1
    elif _y == 2:
        cnt += 1
        ans += _x

    if cnt == x + y:
        print((-ans))
        return

