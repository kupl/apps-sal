import heapq

n, k = map(int,input().split())

q = []
for i in range(n):
    q.append(list(map(int, input().split())))

heapq.heapify(q)

cnt = 0
while cnt < k:
    a, b = heapq.heappop(q)
    cnt += b
    
print(a)
