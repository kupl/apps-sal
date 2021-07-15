import heapq

x, y, z, k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)
c = sorted(list(map(int, input().split())), reverse=True)

que = [(-(a[0]+b[0]+c[0]), 0, 0, 0)]
is_pushed = {(0, 0, 0): 1}
for _ in range(k):
    v, p, q, r = heapq.heappop(que)
    print((-v))
    if p+1 < x and not is_pushed.get((p+1, q, r)):
        heapq.heappush(que, (-(a[p+1]+b[q]+c[r]), p+1, q, r))
        is_pushed[(p+1, q, r)] = 1
    if q+1 < y and not is_pushed.get((p, q+1, r)):
        heapq.heappush(que, (-(a[p]+b[q+1]+c[r]), p, q+1, r))
        is_pushed[(p, q+1, r)] = 1
    if r+1 < z and not is_pushed.get((p, q, r+1)):
        heapq.heappush(que, (-(a[p]+b[q]+c[r+1]), p, q, r+1))
        is_pushed[(p, q, r+1)] = 1

